from itertools import chain

from nltk.corpus import wordnet as wn
import nltk

GREETINGS = [
    "Dear"
]

SIGNS = [
    "Sincerely",
    "Best regards"
]


def _synonyms_preprocessing(lemmas: set[str]) -> set[str]:
    """
    :param lemmas: lemmas as set of strings
    :return: preprocessed lemmas
    """
    preprocessed_lemmas = set()
    for lemma in lemmas:
        lemma = lemma.lower()
        lemma = lemma.replace('_', ' ')
        preprocessed_lemmas.add(lemma)
    return preprocessed_lemmas


nltk.download('wordnet')


def get_synonyms(word: str) -> set[str]:
    """
    :param word: word to get synonyms
    :return: synonyms of the word from WordNet base
    """
    return _synonyms_preprocessing(
        set(chain.from_iterable(
            [word.lemma_names() for word in wn.synsets(word)]
        )
        )
    )
