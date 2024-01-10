from dataclasses import dataclass

@dataclass
class Cheat:
    name: str
    code: str
    enabled: bool = False

    def __post_init__(self):
        self.code = self.code.replace('\n', '&#')

class CheatConverter:
    """
    Convert other cheat formats to the cheat format used by John GBA
    """

