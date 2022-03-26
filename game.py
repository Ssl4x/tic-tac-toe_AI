from cagevalues import *


class Game:
    # private:
    def __char_or_num(self, ret_char: bool) -> list[list[int | str]]:
        it = []
        for i in self.__board:
            it.append([])
            for j in i:
                it.append(it[-1].append(j.get_name() if ret_char else j.get_weight))
        return it

    # public:
    def __init__(self) -> None:
        # создает доску игры, где будут храниться крестики и нолики.
        self.__board: list[list[ClearCage | Cross | Zero]] = [[ClearCage() for _ in range(5)] for _ in range(5)]
        # если True ходят крестики, иначе нолики
        self.__is_cross_turn: bool = True
        
    def turn(self, pos: tuple[int]) -> None | str:
        """Происходит ход игры. В зависимости от очереди хода в определенную клетку ставится крестик или нолик"""
        # проверка занятости клетки
        if type(self.__board[pos[0]][pos[1]]) is ClearCage:
            self.__board[pos[0]][pos[1]] = Cross() if self.__is_cross_turn else Zero()
            self.__is_cross_turn = not self.__is_cross_turn
        else:
            # если клетка занята, возвращат сообщение пользователю
            return "Клетка занята"

    def visualise(self) -> list[list[str]]:
        return self.__char_or_num(ret_char=True)
    
    def nums(self) -> list[list[int]]:
        return self.__char_or_num(ret_char=False)
