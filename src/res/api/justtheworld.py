import re

import requests
from bs4 import BeautifulSoup as Soup
from nltk import WordNetLemmatizer

PARENT_URL = 'http://www.just-the-word.com/main.pl?word={}&mode=combinations'

"""
    <span class="collocstring">
        <a> [content] </a>
    </span>
"""


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
    """
    :param search_request: headword to search in collocation dictionary
    :return: Set of words what can be collocated with headword
    """
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
    return collocation


def is_collocated_words(head: str, child: str) -> bool:
    """
    :param head: word (lemma) to search in collocation dictionary
    :param child: word (lemma) to check collocation dictionary
    :return: Boolean value indicating if words are collocated
    """
    return child in _get_words(head)

#print(_get_words("hello"))
