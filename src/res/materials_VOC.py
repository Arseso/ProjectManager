import os

import pandas as pd
from nltk import SnowballStemmer

_CEFR_WORDLIST_PATH = './res/cefr_dicts/ENGLISH_CERF_WORDS.csv'


def _get_cefr_wordlist() -> pd.DataFrame:
    wordlist = pd.read_csv(_CEFR_WORDLIST_PATH)
    return wordlist


_CEFR_DICTIONARY_DF = None


def _get_cefr_dictionary_df() -> pd.DataFrame:
    global _CEFR_DICTIONARY_DF
    if _CEFR_DICTIONARY_DF is None:
        stemmer = SnowballStemmer('english')
        _CEFR_DICTIONARY_DF = _get_cefr_wordlist()
        _CEFR_DICTIONARY_DF["stemmed"] = _CEFR_DICTIONARY_DF["headword"].apply(lambda x: stemmer.stem(x))
    return _CEFR_DICTIONARY_DF


CEFR_DICTIONARY_DF = _get_cefr_dictionary_df()

COLLOQUIAL_WORDS = ["ain", "gonna", "wanna", "gotta", "kinda", "sorta", "outta", "lotta", "lemme",
                    "gimme", "y", "dunno", "bruh", "fam", "bae", "lit", "dope", "cool", "chill",
                    "yo", "whassup", "wassup", "sup", "bro", "sis", "dude", "homie", "bff", "omg",
                    "lol", "tbh", "idk", "ikr", "smh", "btw", "af", "jk", "omfg", "fyi", "rofl", "btw",
                    "nvm", "lmao", "ftw", "fomo", "squad", "ghosted", "flex", "salty", "savage",
                    "tea", "shade", "yolo", "swag", "clapback", "fire", "thirsty", "basic", "extra",
                    "lowkey", "highkey", "woke", "mood", "shook", "lit", "slay", "vibe", "stan",
                    "fam", "bet", "cap", "no cap", "drip", "finna", "sus", "thicc", "yeet", "sick",
                    "bougie", "bussin", "snatched", "gucci", "hundo", "deadass", "flex", "goat",
                    "jawn", "pog", "simp", "stan", "spill", "stan", "stan", "tea", "tea", "vibe",
                    "vibe", "whip", "whip"]
