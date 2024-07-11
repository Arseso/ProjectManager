import spacy
from nltk import sent_tokenize

from src.models import TextVOC, Word
from src.preprocessing.ca import text_to_model_ca


def _get_plain_text(body: list[str]) -> str:
    """
    Make the plain text from a list of strings.
    :param body: list of strings
    :return: plain text
    """
    return " ".join(body)


def _get_sentences_from_plain(plain_text: str) -> list[str]:
    return sent_tokenize(plain_text)


def _make_trees(sentences: list[str]) -> list[list[Word]]:
    """
    :param sentences: list of str sentences
    :return: list of sentences, where each sentence is a list of Word objects
    """
    spacy_nlp = spacy.load('en_core_web_sm')
    trees = []
    for sentence in sentences:
        doc = spacy_nlp(sentence)
        tokens = []
        for token in doc:
            (
                tokens.append(
                    Word(
                        word=token.text,
                        dep=token.dep_,
                        head=token.head.text,
                        children=[child.text for child in token.children],

                    )
                )
            )
        trees.append(tokens)

    return trees


def text_to_model_voc(text: list[str]) -> TextVOC:
    """
    :param text: text as list of lines
    :return: TextVOC model for analyse VOC metrics
    """
    text_ca = text_to_model_ca(text)
    plain_text = _get_plain_text(text_ca.body)
    sentences = _get_sentences_from_plain(plain_text)
    voc = TextVOC(
        ca=text_ca,
        body_as_plain_text=plain_text,
        body_as_sentences=sentences,
        sentences_as_trees=_make_trees(sentences)
    )
    return voc
