import random
from player import Player


class SimpleBot(Player):
    def __init__(self, name: str):
        self._past_guesses = []
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def guess(self, num_slots: int) -> tuple[int, ...]:
        possible_numbers = list(range(1, num_slots + 1))

        while True:
            random.shuffle(possible_numbers)
            guess = tuple(possible_numbers)

            if guess not in self._past_guesses:
                print(f"{self._name} guessed {guess}")
                self._past_guesses.append(guess)
                return guess

    def process_result(self, result: int) -> None:
        print(f"{self._name} got {result} positions correct.\n")
