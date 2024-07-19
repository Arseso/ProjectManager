import os
import re

import requests
from bs4 import BeautifulSoup as Soup
from nltk import WordNetLemmatizer
import pandas as pd

PARENT_URL = 'http://www.just-the-word.com/main.pl?word={}&mode=combinations'

"""
    <span class="collocstring">
        <a> [content] </a>
    </span>
"""

COLLOCATION_DF: pd.DataFrame = None
IS_CACHE_FILE_EDITED = False


def _get_cache() -> bool:
    global COLLOCATION_DF
    if COLLOCATION_DF is not None:
        return True
    try:
        COLLOCATION_DF = pd.read_csv("./.cache/collocation_dict.csv")
        return True
    except:
        print("[CACHE] Collocation dictionary not found")
        _init_cache_file()
        return False


def _init_cache_file():
    global COLLOCATION_DF
    os.mkdir("./.cache")
    COLLOCATION_DF = pd.DataFrame(columns=["head", "child"])


def _save_cache():
    global COLLOCATION_DF
    COLLOCATION_DF.to_csv('./.cache/collocation_dict.csv', index=False)


def _get_page(search_request: str) -> Soup:
    """
    :param search_request: headword to search in collocation dictionary
    :return: soup object of the page
    """
    page = requests.get(PARENT_URL.format(search_request))
    soup = Soup(page.content, 'html.parser')
    return soup


wnl = WordNetLemmatizer()


def _preprocessed_word(word: str) -> str:
    word = word.lower()
    word = word.replace(' ', '')
    if re.match('^[a-z]+$', word):
        # word = wnl.lemmatize(word)
        return word
    return ""


def _get_words(search_request: str) -> set[str]:
    global IS_CACHE_FILE_EDITED, COLLOCATION_DF
    """
    :param search_request: headword to search in collocation dictionary
    :return: Set of words what can be collocated with headword
    """
    if len(COLLOCATION_DF[COLLOCATION_DF['head'] == search_request]) == 0:
        soup = _get_page(search_request)

        # Get <span> class="collocstring" tags
        span_tags = soup.find_all('span', class_="collocstring", recursive=True)
        collocation = set()
        for span_tag in span_tags:
            # Get <a>
            a_tag = span_tag.findNext('a')
            # Split <a> by " " and get collocation word
            for word in a_tag.text.split(" "):
                if _preprocessed_word(word) != "" and _preprocessed_word(word) != search_request:
                    collocation.add(_preprocessed_word(word))
        IS_CACHE_FILE_EDITED = True
        for colloc in collocation:
            COLLOCATION_DF.loc[len(COLLOCATION_DF.index)] = [search_request, colloc]
        return collocation
    return COLLOCATION_DF[COLLOCATION_DF['head'] == search_request].child.values


def is_collocated_words(head: str, child: str) -> bool:
    """
    :param head: word (lemma) to search in collocation dictionary
    :param child: word (lemma) to check collocation dictionary
    :return: Boolean value indicating if words are collocated
    """
    _get_cache()
    resp = child in _get_words(head)
    if IS_CACHE_FILE_EDITED:
        _save_cache()
    return resp

#print(_get_words("hello"))
