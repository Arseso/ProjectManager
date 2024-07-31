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


def _find_to(text: list[str]) -> tuple[str | None, list[str]]:
    """
    :param text: list of lines from email
    :return: recipient's address, None if didn't find one
    """
    match = re.search(PATTERN_MAIL, text[0])

    if match:
        email = match.group(0)
        return email, text[1:]
    else:
        return None, text


def _find_subject(text: list[str]) -> tuple[str | None, list[str]]:
    """
    :param text: list of lines from email
    :return: message subject string, None if didn't find one
    """
    try:
        subj = text[0].split(": ", 1)[1]
        return subj, text[:1]
    except IndexError:
        return None, text


def _find_name_from_greeting(text: list[str]) -> tuple[str | None, list[str]]:
    """
    :param text: list of lines from email
    :return: recipient's name from greeting, None if didn't find one
    """
    pattern = rf"^({PATTERN_GREETING})\s*(.*)"
    match = re.match(pattern, text[0])
    if match:
        return match.group(2).replace(",", ""), text[1:]
    else:
        return None, text


def _find_body(text: list[str]) -> list[str] | None:
    """
    :param text: list of lines from email
    :return: email body as list of lines, None if didn't find one
    """
    return text if text else None


def _find_sign(text: list[str]) -> str | None:
    """
    :param text: list of lines from email
    :return: sign from email, None if didn't find one
    """

    if re.match(PATTERN_SIGN, text[-1]):
        return text[-1], text[:-2]
    else:
        return None, text


def text_to_model_ca(text: list[str]) -> TextCA:
    """
    :param text: list of lines from email
    :return: model from text for analyze CA metrics
    """
    
    text = _preprocessing_pipeline(text)
    _to, text = _find_to(text)
    _subj, text = _find_subject(text)
    _sign, text = _find_sign(text)
    _name, text = _find_name_from_greeting(text)
    _body = _find_body(text)
    model = TextCA(
        to =_to,
        subject = _subj,
        greeting_name = _name,
        sign = _sign,
        body = _body
        
    )
    return model
