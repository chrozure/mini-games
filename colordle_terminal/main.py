import random
from game import Game
from human_player import HumanPlayer
from simple_bot import SimpleBot


def main():
    players = [HumanPlayer("User"), SimpleBot("Simple Bot")]
    game = Game(players)

    game.initialize()
    while game.is_running:
        game.play_round()


if __name__ == "__main__":
    main()
