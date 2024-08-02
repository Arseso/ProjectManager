from dataclasses import dataclass


# Новый csv 0/1 + метрики, количество абзацев
# тесты к критериям ввод - csv
# инфо об авторе мб разд на неск строк

# Marks: 2 - "+", 1 - "+-", 0 - "-"
@dataclass
class Response:
    # Communicative Achievement/Content
    CA1: float = 0
    CA11: float = 0
    CA12: float = 0
    CA13: float = 0
    CA14: float = 0
    CA15: float = 0
    CA16: float = 0
    CA17: float = 0
    CA2: float = 0
    # Organization
    ORG1: float = 0
    ORG2: float = 0
    ORG22: float = 0
    ORG23: float = 0
    ORG24: float = 0
    ORG25: float = 0
    ORG3: float = 0
    # Vocabulary
    VOC1: float = 0
    VOC2: float = 0
    VOC3: float = 0
    # Grammar
    GR1: float = 0
    GR2: float = 0
    GR3: float = 0

    # Metrics

    UNIQ_W_PROPORTION: float = 0
    ORTHOGRAPHY_ERRORS: float = 0
    COLLOQUIAL_WORDS: float = 0
    COLLOCATION_ERRORS: float = 0

    CEFR_PROPORTIONS: tuple = None

    CEFR_PROPORTIONS: tuple = None

    def values(self, module: str = None, as_num = False) -> list[str]:
        """
        :param module: "CA", "ORG", "VOC", "GR", "metrics"
        :paeam as_num: if true, return module as float values
        :return: list of program responses for this module
        """
        if module is None:
            raise ValueError("Module must be provided")
        
        # CA

        elif module == "CA" and not as_num:
            return ["+" if metric == 1
                    else "-" if metric == 0
            else "+-"
                    for metric in
                    [self.CA1, self.CA11, self.CA12, self.CA13, self.CA14, self.CA15, self.CA16, self.CA17, self.CA2]]
        
        elif module == "CA" and as_num:
            return [self.CA1, self.CA11, self.CA12, self.CA13, self.CA14, self.CA15, self.CA16, self.CA17, self.CA2]
        

        # ORG

        elif module == "ORG" and not as_num:
            return ["+" if metric == 1
                    else "-" if metric == 0
            else "+-"
                    for metric in [self.ORG1, self.ORG2, self.ORG22, self.ORG23, self.ORG24, self.ORG25, self.ORG3]]
        
        elif module == "ORG" and as_num:
            return [self.ORG1, self.ORG2, self.ORG22, self.ORG23, self.ORG24, self.ORG25, self.ORG3]
        
        # VOC

        elif module == "VOC" and not as_num:
            return ["+" if metric == 1
                    else "-" if metric == 0
            else "+-"
                    for metric in [self.VOC1, self.VOC2, self.VOC3]]
        
        elif module == "VOC" and as_num:
            return [self.VOC1, self.VOC2, self.VOC3]
        
        # GR

        elif module == "GR" and not as_num:
            return ["+" if metric == 1
                    else "-" if metric == 0
            else "+-"
                    for metric in [self.GR1, self.GR2, self.GR3]]
        
        elif module == "GR" and as_num:
            return [self.GR1, self.GR2, self.GR3]
        
        # Metrics

        elif module == "metrics":
            return [self.UNIQ_W_PROPORTION, self.ORTHOGRAPHY_ERRORS, self.COLLOQUIAL_WORDS, self.COLLOCATION_ERRORS, *self.CEFR_PROPORTIONS]


@dataclass
class TextCA:
    to: str | None
    subject: str | None
    greeting_name: str | None
    body: list[str] | None
    sign: str | None


@dataclass
class Word:
    word: str
    dep: str
    head: str | None
    children: list[str] | None


@dataclass
class TextVOC:
    ca: TextCA | None
    body_as_plain_text: str | None
    body_as_sentences: list[str] | None
    sentences_as_trees: list[list[Word]] | None
