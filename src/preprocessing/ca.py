from models import TextCA
from res.materials_CA import GREETINGS
import re

PATTERN_MAIL = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
PATTERN_GREETING = "|".join(re.escape(s) for s in GREETINGS)
PATTERN_SIGN = r"[A-Z][a-z]+ [A-Z][a-z]+"


def _preprocessing_pipeline(text: list[str]) -> list[str]:
    """

    :param text: list of lines from email
    :return: list of lines from email after preprocessing
    """
    result = []
    for line in text:
        line = line.replace("\n", "")
        if line == "" or line.isspace():
            continue
        line = line.lstrip()
        line = line.rstrip()
        result.append(line)
    return result


def _find_to(text: list[str]) -> str | None:
    """
    :param text: list of lines from email
    :return: recipient's address, None if didn't find one
    """
    match = re.search(PATTERN_MAIL, text[0])

    if match:
        email = match.group(0)
        return email
    else:
        return None


def _find_subject(text: list[str]) -> str | None:
    """
    :param text: list of lines from email
    :return: message subject string, None if didn't find one
    """
    try:
        subj = text[1].split(": ", 1)[1]
        return subj
    except IndexError:
        return None


def _find_name_from_greeting(text: list[str]) -> str | None:
    """
    :param text: list of lines from email
    :return: recipient's name from greeting, None if didn't find one
    """
    pattern = rf"^({PATTERN_GREETING})\s*(.*)"
    match = re.match(pattern, text[2])
    if match:
        return match.group(2).replace(",", "")
    else:
        return None


def _find_body(text: list[str]) -> list[str] | None:
    """
    :param text: list of lines from email
    :return: email body as list of lines, None if didn't find one
    """
    body = text[3:-2]
    return body if body else None


def _find_sign(text: list[str]) -> str | None:
    """
    :param text: list of lines from email
    :return: sign from email, None if didn't find one
    """

    if re.match(PATTERN_SIGN, text[-1]):
        return text[-1]
    else:
        return None


def text_to_model_ca(text: list[str]) -> TextCA:
    """
    :param text: list of lines from email
    :return: model from text for analyze CA metrics
    """
    text = _preprocessing_pipeline(text)
    model = TextCA(
        _find_to(text),
        _find_subject(text),
        _find_name_from_greeting(text),
        _find_body(text),
        _find_sign(text)
    )
    return model
