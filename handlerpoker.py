from utils import move_and_click


class HandlerPoker:
    def __init__(self):
        self.count = 0
        self.list_poke = [(128, 229), (112, 261), (110, 309), (116, 354), (118, 399), (144, 441)]

    def check_poke_length(self):
        self.count = self.count % len(self.list_poke)

    def next(self):
        self.count = self.count + 1
        self.check_poke_length()
        move_and_click(self.list_poke[self.count], 'right')

    def previous(self):
        self.count = self.count - 1
        self.check_poke_length()
        move_and_click(self.list_poke[self.count], 'right')
