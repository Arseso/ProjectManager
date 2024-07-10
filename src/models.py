from dataclasses import dataclass


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

    def values(self, module: str = None) -> list[str]:
        """
        :param module: "CA", "ORG", "VOC", "GR"
        :return: list of program responses for this module
        """
        if module is None:
            raise ValueError("Module must be provided")
        elif module == "CA":
            return ["+" if metric == 1
                    else "-" if metric == 0
                    else "+-"
                    for metric in [self.CA1, self.CA11, self.CA12, self.CA13, self.CA14, self.CA15, self.CA16, self.CA17, self.CA2]]
        elif module == "ORG":
            return ["+" if metric == 1
                    else "-" if metric == 0
                    else "+-"
                    for metric in [self.ORG1, self.ORG2, self.ORG22, self.ORG23, self.ORG24, self.ORG25, self.ORG3]]
        elif module == "VOC":
            return ["+" if metric == 1
                    else "-" if metric == 0
                    else "+-"
                    for metric in [self.VOC1, self.VOC2, self.VOC3]]
        elif module == "GR":
            return ["+" if metric == 1
                    else "-" if metric == 0
                    else "+-"
                    for metric in [self.GR1, self.GR2, self.GR3]]


@dataclass
class TextCA:
    to: str | None
    subject: str | None
    greeting_name: str | None
    body: list[str] | None
    sign: str | None
