import re

import requests
from bs4 import BeautifulSoup as Soup

PARENT_URL = 'https://m.freecollocation.com/browse/{}'

"""
    PATH to word word elements:
    body -> div id=__nuxt -> 
    div class=mx-auto p-3 max-w-2xl leading-7 text-base -> 
    div (2nd) -> div class=item -> p (all after first) -> 
    b tags, words separated by: "|", ","
"""


def _get_page(search_request: str) -> Soup:
    """
    :param search_request: headword to search in collocation dictionary
    :return: soup object of the page
    """
    page = requests.get(PARENT_URL.format(search_request))
    soup = Soup(page.content, 'html.parser')
    return soup


def _preprocessed_word(word: str) -> str:
    word = word.lower()
    word = word.replace(' ', '')
    if re.match('^[a-z]+$', word):
        return word
    return ""


def _get_words(search_request: str) -> set[str]:
    soup = _get_page(search_request)

    # Get <p> wout class attribute
    p_tags = soup.find_all('p', class_=False, recursive=True)

    collocation = set()
    for p_tag in p_tags:

        # Get <b>
        b_tags = p_tag.find_all_next('b')

        # Split <b> by "|" and ","
        for b_tag in b_tags:
            for words in b_tag.text.split("|"):
                for word in words.split(","):
                    if len(_preprocessed_word(word)) != 0:
                        collocation.add(_preprocessed_word(word))
    return collocation


def is_collocated_words(head: str, child: str) -> bool:
    """
    :param head: word (lemma) to search in collocation dictionary
    :param child: word (lemma) to check collocation dictionary
    :return: Boolean value indicating if words are collocated
    """
    return child in _get_words(head)
