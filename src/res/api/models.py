from dataclasses import dataclass


@dataclass
class RequestLanguagetool:
    text: str
    language: str = "en"



@dataclass
class ResponseLanguagetool:
    matches: list
