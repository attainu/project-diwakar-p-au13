class Board:
    def __init__(self):
        self.board = [None for x in range(101)]

    def populate(self, snakes, ladders):

        for snake in snakes:
            start = snake.get_start()
            self.board[start] = snake

        for ladder in ladders:
            start = ladder.get_start()
            self.board[start] = ladder

        return self.board
