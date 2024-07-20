import re
from collections import Counter

import nltk
import pandas as pd
import tqdm
from nltk.stem import WordNetLemmatizer
import env
from env import VOC2_PLUS_ORTH_THRESHOLD, VOC2_PLUS_COLL_PROPORTION, \
    VOC2_MINUS_COLL_PROPORTION, VOC2_MINUS_ORTH_THRESHOLD, VOC1_PLUS_UNIQUE_PROPORTION
from models import TextVOC, Response
from preprocessing.voc import text_to_model_voc, \
    voc_1_preprocessed_text, voc_2_preprocessed_text
from res.materials_VOC import CEFR_DICTIONARY_DF, COLLOQUIAL_WORDS
from res.api.languagetool import get_orthography_errors
from res.api.justtheworld import is_collocated_words
from res.wordsDegree.WordsDegree import get_degrees

nltk.download('stopwords')


def _preprocessed_text(text: list[str]) -> TextVOC:
    return text_to_model_voc(text)


<<<<<<< HEAD
def _voc_1(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 1 metric
=======
def _voc_1(text: TextVOC) -> tuple[float, float]:
    """
    :param text: TextCA model
    :return: float value of VOC 1 metric, float value of unique words proportion
>>>>>>> dev
    """
    preprocessed_text, words_count = voc_1_preprocessed_text(text=text.body_as_plain_text, stemming=False)
    cerf_dict = CEFR_DICTIONARY_DF
    cerf_levels, undefined = get_degrees(preprocessed_text)
    for token in undefined:
        if token in cerf_dict.headword.values:
            cerf_levels.append(cerf_dict[cerf_dict.headword == token].CEFR.values[0])
        else:
            cerf_levels.append("A1")
    cerf_counter = Counter(cerf_levels)
    print(f"Unique words proportion: {len(preprocessed_text) / words_count}")
    print(f"Unique words CERF levels proportion:"
          f" A1:{cerf_counter['A1'] / len(cerf_levels):.2f},"
          f" A2:{cerf_counter['A2'] / len(cerf_levels):.2f},"
          f" B1:{cerf_counter['B1'] / len(cerf_levels):.2f},"
          f" B2:{cerf_counter['B2'] / len(cerf_levels):.2f},"
          f" C1:{cerf_counter['C1'] / len(cerf_levels):.2f},"
          f" C2:{cerf_counter['C2'] / len(cerf_levels):.2f},")
    if len(preprocessed_text) / words_count >= VOC1_PLUS_UNIQUE_PROPORTION:
<<<<<<< HEAD
        return 1
    return 0


def _voc_2(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 2 metric
=======
        return 1, len(preprocessed_text) / words_count
    return 0, len(preprocessed_text) / words_count


def _voc_2(text: TextVOC) -> tuple[float, int, int]:
    """
    :param text: TextCA model
    :return: float value of VOC 2 metric, int orthography errors, int colloquial words
>>>>>>> dev
    """
    orthography_errors = get_orthography_errors(text=text)
    preprocessed_text, words_count = voc_2_preprocessed_text(text=text)
    colloquial_count = 0
    for token in preprocessed_text:
        if token in COLLOQUIAL_WORDS:
            colloquial_count += 1
    print(f"VOC2; OPTH_ER:{orthography_errors}, COLL:{colloquial_count}")
    if orthography_errors <= VOC2_PLUS_ORTH_THRESHOLD and colloquial_count/words_count <= VOC2_PLUS_COLL_PROPORTION:
<<<<<<< HEAD
        return 1
    if orthography_errors <= VOC2_MINUS_ORTH_THRESHOLD and colloquial_count/words_count <= VOC2_MINUS_COLL_PROPORTION:
        return 0.5
    else:
        return 0


def _voc_3(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 3 metric
=======
        return 1, orthography_errors, colloquial_count
    if orthography_errors <= VOC2_MINUS_ORTH_THRESHOLD and colloquial_count/words_count <= VOC2_MINUS_COLL_PROPORTION:
        return 0.5, orthography_errors, colloquial_count
    else:
        return 0, orthography_errors, colloquial_count


def _voc_3(text: TextVOC) -> tuple[float, int]:
    """
    :param text: TextCA model
    :return: float value of VOC 3 metric, int collocation errors
>>>>>>> dev
    """
    errors_df = pd.DataFrame(columns=["head", "child"])

    errors = 0
    stopwords = set(nltk.corpus.stopwords.words('english'))
    for i in tqdm.trange(len(text.sentences_as_trees), desc="VOC3; Sentences processed"):
        for word_object in text.sentences_as_trees[i]:
            head = word_object.head.lower()
            if not re.match(r'^[a-z]+$', head) or head in stopwords or head == env.COMPANY_NAME:
                continue
            for child in word_object.children:
                # wnl = WordNetLemmatizer()
                # child = wnl.lemmatize(child)

                child = child.lower()
                if not re.match(r'^[a-z]+$', child) or child in stopwords or child == env.COMPANY_NAME:
                    continue
                if not is_collocated_words(head, child):
                    errors_df.loc[len(errors_df.index)] = [head, child]
                    errors += 1
    errors_df.to_csv("./.cache/collocation_errors.csv", index=False, mode="a")
    print(f"VOC3; ERRORS:{errors}")
<<<<<<< HEAD
    if errors > 2: return 0
    if errors > 0: return 0.5
    return 1
=======
    if errors > 2: return 0, errors
    if errors > 0: return 0.5, errors
    return 1, errors
>>>>>>> dev


def get_voc_metrics(resp: Response, text: list[str]) -> Response:
    """
    :param resp: Response object, where VOC metrics will be changed
    :param text: text as list of lines to analyze
    :return: Response object with VOC metrics
    """
    text = _preprocessed_text(text)
<<<<<<< HEAD
    resp.VOC1 = _voc_1(text)
    resp.VOC2 = _voc_2(text)
    resp.VOC3 = _voc_3(text)
=======
    resp.VOC1, resp.UNIQ_W_PROPORTION = _voc_1(text)
    resp.VOC2, resp.ORTHOGRAPHY_ERRORS, resp.COLLOQUIAL_WORDS = _voc_2(text)
    resp.VOC3, resp.COLLOCATION_ERRORS = _voc_3(text)
>>>>>>> dev
    return resp
