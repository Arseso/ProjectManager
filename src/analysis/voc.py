import re
from collections import Counter

import nltk

from src.env import VOC2_PLUS_ORTH_THRESHOLD, VOC2_PLUS_COLL_PROPORTION, \
    VOC2_MINUS_COLL_PROPORTION, VOC2_MINUS_ORTH_THRESHOLD, VOC1_PLUS_UNIQUE_PROPORTION
from src.models import TextVOC, Response
from src.preprocessing.voc import text_to_model_voc, \
    voc_1_preprocessed_text, voc_2_preprocessed_text
from src.res.materials_VOC import CEFR_DICTIONARY_DF, COLLOQUIAL_WORDS
from src.res.api.languagetool import get_orthography_errors

nltk.download('stopwords')


def _preprocessed_text(text: list[str]) -> TextVOC:
    return text_to_model_voc(text)


def _voc_1(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 1 metric
    """
    preprocessed_text, words_count = voc_1_preprocessed_text(text=text)
    cerf_dict = CEFR_DICTIONARY_DF
    cerf_levels = []
    for token in preprocessed_text:
        if token in cerf_dict.stemmed.values:
            cerf_levels.append(cerf_dict[cerf_dict.stemmed == token].CEFR.values[0])
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
        return 1
    return 0


def _voc_2(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 2 metric
    """
    orthography_errors = get_orthography_errors(text=text)
    preprocessed_text, words_count = voc_2_preprocessed_text(text=text)
    colloquial_count = 0
    for token in preprocessed_text:
        if token in COLLOQUIAL_WORDS:
            colloquial_count += 1
    print(f"VOC2; OPTH_ER:{orthography_errors}, COLL:{colloquial_count}")
    if orthography_errors <= VOC2_PLUS_ORTH_THRESHOLD and colloquial_count/words_count <= VOC2_PLUS_COLL_PROPORTION:
        return 1
    if orthography_errors <= VOC2_MINUS_ORTH_THRESHOLD and colloquial_count/words_count <= VOC2_MINUS_COLL_PROPORTION:
        return 0.5
    else:
        return 0


def _voc_3(text: TextVOC) -> float:
    """
    :param text: TextCA model
    :return: float value of VOC 3 metric
    """


def get_voc_metrics(resp: Response, text: list[str]) -> Response:
    """
    :param resp: Response object, where VOC metrics will be changed
    :param text: text as list of lines to analyze
    :return: Response object with VOC metrics
    """
    text = _preprocessed_text(text)
    resp.VOC1 = _voc_1(text)
    resp.VOC2 = _voc_2(text)
    resp.VOC3 = _voc_3(text)
    return resp
