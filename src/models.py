from dataclasses import dataclass


# Marks: 2 - "+", 1 - "+-", 0 - "-"
@dataclass
class Response:
    # Communicative Achievement/Content
    CA1: int = 0
    CA11: int = 0
    CA12: int = 0
    CA13: int = 0
    CA14: int = 0
    CA15: int = 0
    CA16: int = 0
    CA17: int = 0
    # Organization
    ORG1: int = 0
    ORG2: int = 0
    ORG22: int = 0
    ORG23: int = 0
    ORG24: int = 0
    ORG25: int = 0
    ORG3: int = 0
    # Vocabulary
    VOC1: int = 0
    VOC2: int = 0
    VOC3: int = 0
    # Grammar
    GR1: int = 0
    GR2: int = 0
    GR3: int = 0

    def values(self, module: str = None) -> list[int]:
        """
        :param module: "CA", "ORG", "VOC", "GR"
        :return: list of program responses for this module
        """
        if module is None:
            raise ValueError("Module must be provided")
        elif module == "CA":
            return [self.CA1, self.CA11, self.CA12, self.CA13, self.CA14, self.CA15, self.CA16, self.CA17]
        elif module == "ORG":
            return [self.ORG1, self.ORG2, self.ORG22, self.ORG23, self.ORG24, self.ORG25, self.ORG3]
        elif module == "VOC":
            return [self.VOC1, self.VOC2, self.VOC3]
        elif module == "GR":
            return [self.GR1, self.GR2, self.GR3]