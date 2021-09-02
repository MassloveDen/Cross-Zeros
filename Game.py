from enum import Enum

import pygame


CELL_SIZE = 50
refresh_rate = 60

class Cell(Enum):

    VOID = 0
    CROSS = 1
    ZERO = 2


class Player:
    """
    Player class, type sign and name
    """
    def __init__(self, name, cell_type):
        self.name = name
        self.cell_type = cell_type

class GameField:
    def __init__(self):
        self.height = 3
        self.width = 3
        self.cells = [[Cell.VOID]*self.width for _ in range(self.height)]


class GameFieldView:
    """
    Paint new game field and position to click
    """
    def __init__(self, field):
        # signs and fields position
        self._field = field
        self._height = field.height * CELL_SIZE
        self._width = field.width * CELL_SIZE

    def draw(self):
        pass

    def check_coord_correct(self, x, y):
        return True  # TODO: self._height needed

    def get_coords(self, x, y):
        return 0, 0  # TODO: find click field


class GameRoundManager:
    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.field = GameField()

    def handle_click(self, i, j):
        player = self._players[self._current_player]
        print("click_handled", i, j)


class GameWindow:
    def __init__(self):
        pygame.init()

        self._width = 800
        self._height = 600
        self._title = 'Cross & Zeroes'
        self._screen = pygame.display.set_mode((self._width, self._height))

        player1 = Player('P1', Cell.CROSS)
        player2 = Player('P2', Cell.ZERO)
        self._game_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_manager.field)

    def main_loop(self):
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    x, y = mouse_pos
                    if self._field_widget.check_coord_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(refresh_rate)

def main():
    window = GameWindow()
    window.main_loop()
    print("Game over!")


if __name__ == "__main__":
    main()

