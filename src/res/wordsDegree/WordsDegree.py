import spacy
import os


def take_dicts(dicts_dir="./res/wordsDegree/oxford-dictionary"):

    this_general_dict = {}

    for root, dirs, files in os.walk(dicts_dir):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)

                with open(path, "r") as f:
                    text = f.read()
                    words_list = text.split("\n")
                    for word in words_list:
                        word = word.strip().split()
                        if not word:
                            continue
                        this_general_dict[word[0]] = file.replace(".txt", "")

    return this_general_dict


print("Start making general dict")
general_dict = take_dicts()
nlp = spacy.load("en_core_web_sm")


def get_degrees_for_one_word(word: str) -> str:


    modal_verb_list = ["can", "could", "may", "might", "will", "shall", "would", "should", "must"]


    for token in nlp(word):
        word = token.lemma_

    degree = general_dict.get(word)

    return degree


def get_degrees(words_list):
    """ Возвращает для каждого слова из списка его уровень.
        Если слово не найдено, оно сохраняется в списке нераспознанных слов. """
    result = []
    unidentified_words = []

    for word in words_list:
        degree = get_degrees_for_one_word(word)

        if degree is None:
            unidentified_words.append(word)
            continue

        result.append(degree)



    return result, unidentified_words
