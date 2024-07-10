from src.models import Response

from src.models import TextCA
from src.preprocessing.ca import text_to_model_ca


def _preprocessed_text(text: list[str]) -> TextCA:
    """
    :param text: email as list of lines
    :return: TextCA model
    """
    return text_to_model_ca(text)


def _org_22(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of ORG 2.2 metric
    """
    return 1 if len(text.greeting_name) > 0 else 0


def _org_23(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of ORG 2.3 metric
    """
    return 1 if len(text.greeting_name) > 0 else 0


def _org_24(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of ORG 2.4 metric
    """
    if len(text.body) > 1:
        return 1
    return 0


def _org_25(text: TextCA) -> float:
    """
    :param text: TextCA model
    :return: float value of ORG 2.5 metric
    """
    if len(text.to) > 0 \
            and len(text.greeting_name) > 0 \
            and len(text.body) > 1 \
            and len(text.sign) > 0:
        return 1
    return 0


def get_org_metrics(resp: Response, text: list[str]) -> Response:
    """
    :param resp: Response object, where CA metrics will be changed
    :param text: text as list of lines to analyze
    :return: Response object with CA metrics
    """
    text = _preprocessed_text(text)
    resp.ORG22 = _org_22(text)
    resp.ORG23 = _org_23(text)
    resp.ORG24 = _org_24(text)
    resp.ORG25 = _org_25(text)
    return resp
