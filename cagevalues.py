class __CageValue:
    """Basic class for inheritance"""

    def __init__(self) -> None:
        self.__name: str
        self.__weight: int

    def get_name(self) -> str:
        return self.__name

    def get_weight(self) -> int:
        return self.__weight

class Zero(__CageValue):
    def __init__(self) -> None:
        super().__init__()
        self.__name = "O"
        self.weight = 1

class ClearCage(__CageValue):
    def __init__(self) -> None:
        super().__init__()
        self.__name = " "
        self.__weight = 0

class Cross(__CageValue):
    def __init__(self) -> None:
        super().__init__()
        self.__name = "X"
        self.weight = 2
