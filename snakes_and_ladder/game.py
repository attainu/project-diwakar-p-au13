from dice import Dice
from snake import Snake
from ladder import Ladder
from player import Player
from board import Board


class Game:
    def __init__(self):
        self.winner = None
        self.snakes = []
        self.ladders = []
        self.players = []

    def configure(self):
        print('\n*************** Configure Board ***************')
        snakes_count = int(input('\nEnter number of snakes: '))
        for x in range(snakes_count):
            pos = input(
                f'\nEnter the start & end position of snake #{x+1}: ').split(',')
            self.snakes.append(Snake(int(pos[0]), int(pos[1])))

        ladders_count = int(input('\nEnter number of ladders: '))
        for x in range(ladders_count):
            pos = input(
                f'\nEnter the start & end position of ladder #{x+1}: ').split(',')
            self.ladders.append(Ladder(int(pos[0]), int(pos[1])))

        players_count = int(input('\nEnter number of players (min. 2): '))
        for x in range(players_count):
            playerName = input(f'\nEnter name of Player #{x+1}: ')
            self.players.append(Player(playerName, 1))

    def play(self):
        board = Board().populate(self.snakes, self.ladders)
        dice = Dice()

        while self.winner == None:
            for player in self.players:
                dice_value = dice.roll()
                player.move(dice_value)

                encounter = board[player.position]
                if encounter:
                    end = encounter.end
                    print(f"{encounter.message}")
                    player.move(end, encounter=True)

                if player.is_winner:
                    self.winner = player
                    break
                input()

        print("\n*************** GAME OVER ***************")
        print(f"Player {self.winner.name} won the game.")
        print("*************** GAME OVER ***************\n")


if __name__ == "__main__":
    game = Game()
    game.configure()
    game.play()
