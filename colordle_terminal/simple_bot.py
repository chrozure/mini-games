import random
from player import Player


class SimpleBot(Player):
    def __init__(self, name: str = ""):
        self.past_guesses = []
        self.name = name

    def guess(self, num_slots: int) -> tuple[int, ...]:
        possible_numbers = list(range(1, num_slots + 1))

        while True:
            random.shuffle(possible_numbers)
            guess = tuple(possible_numbers)

            if guess not in self.past_guesses:
                print(f"The bot guessed {guess}")
                self.past_guesses.append(guess)
                return guess

    def process_result(self, result: int) -> None:
        print(f"The bot got {result} positions correct.\n")
