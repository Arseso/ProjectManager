from models import TextCA, Response
from res.materials_CA import get_synonyms
from preprocessing.ca import text_to_model_ca
import env as env
import nltk.stem.snowball as snowball

stemmer = snowball.SnowballStemmer("english")


def _preprocessed_text(text: list[str]) -> TextCA:
    """
    :param text: email as list of lines
    :return: TextCA model
    """
    return text_to_model_ca(text)


def _ca_11(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.1 metric
    """
    return 1 if len(text.greeting_name) > 0 else 0


def _ca_12(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.2 metric
    """
    return 1 if text.to == env.EMAIL else 0


def _ca_13(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.3 metric
    """
    for line in text.body:
        if env.COMPANY_NAME.lower() in line.lower():
            return 1
    return 0


def _ca_14(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.4 metric
    """

    Изменить

    key_words = get_synonyms("writing")
    key_words = set([stemmer.stem(word) for word in key_words])
    key_words.add("writing")

    for line in text.body:
        for word in key_words:
            if word in line.lower():
                return 1
    return 0


def _ca_15(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.5 metric
    """

    for line in text.body:
        if env.VACANCY_NAME[0].lower() in line.lower()\
        or env.VACANCY_NAME[1].lower() in line.lower():
            return 1
    return 0


def _ca_16(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.6 metric
    """
    key_words = set(env.VACANCY_RESPONSIBILITIES)
    for word in env.VACANCY_RESPONSIBILITIES:
        for syn in get_synonyms(word):
            key_words.add(stemmer.stem(syn))

    for line in text.body:
        for word in key_words:
            if word in line.lower():
                return 1
    return 0


def _ca_17(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of CA 1.7 metric
    """
    key_words = get_synonyms("thanks")
    for line in text.body:
        for word in key_words:
            if stemmer.stem(word) in line.lower():
                return 1
    return 0


def get_ca_metrics(resp: Response, text: list[str]) -> Response:
    """
    :param resp: Response object, where CA metrics will be changed
    :param text: text as list of lines to analyze
    :return: Response object with CA metrics
    """
    text = _preprocessed_text(text)
    resp.CA11 = _ca_11(text)
    resp.CA12 = _ca_12(text)
    resp.CA13 = _ca_13(text)
    resp.CA14 = _ca_14(text)
    resp.CA15 = _ca_15(text)
    resp.CA16 = _ca_16(text)
    resp.CA17 = _ca_17(text)
    return resp
