import requests
import jsons

from src.models import TextVOC
from src.res.api.models import RequestLanguagetool, ResponseLanguagetool

URL = "https://api.languagetoolplus.com/v2/check"


def _send_request(text: str) -> ResponseLanguagetool:
    """
    :param text: text to check
    :return: ResponseLanguagetool object
    """
    req_data = RequestLanguagetool(text)
    response = requests.post(URL, data=jsons.dump(req_data))
    return jsons.load(response.json(), ResponseLanguagetool)


def get_orthography_errors(text: TextVOC) -> int:
    """
    :param text: text to check on orthography errors
    :return: number of orthography errors
    """
    if len(text.body_as_plain_text) > 1500:
        characters = ""
        errors = 0
        for line in text.ca.body:
            if len(" ".join([characters, line])) > 1500:
                response = _send_request(characters)
                errors += len(response.matches)
                characters = ""
            else:
                characters += line
        response = _send_request(characters)
        errors += len(response.matches)
        return errors

    response = _send_request(text.body_as_plain_text)
    return len(response.matches)
