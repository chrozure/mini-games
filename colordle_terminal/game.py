"""
game.py
Implements the Game class, which is responsible for
managing all the players and controlling the gameplay
"""

import random
from player import Player


class Game:
    def __init__(self,  players: list[Player]):
        self.is_running = True
        self.round_number = 0

        self._players = players
        self._is_easy_mode = False
        self._num_slots = 5
        self._correct_answer = (1, 2, 3, 4, 5)

    def initialize(self) -> None:
        # Select difficulty
        easy_mode_input = input("Would you like to play on easy mode? (y/n): ").lower()
        if easy_mode_input == 'y':
            self._is_easy_mode = True

        # Get number of slots
        while True:
            num_slots = int(input("Enter number of slots (3 - 7): "))
            if num_slots <= 0:
                print(f"You can't guess {num_slots} numbers...")
            elif num_slots < 3:
                print("That's too easy!")
            elif num_slots > 7:
                print("Trust me that will take too long :)")
            else:
                self._num_slots = num_slots
                break

        print("Generating answer...")
        possible_numbers = list(range(1, num_slots + 1))
        random.shuffle(possible_numbers)
        self._correct_answer = tuple(possible_numbers)

    def play_round(self):
        self.round_number += 1
        print("--------------------------------------")
        print(f"Round {self.round_number}")

        for player in self._players:
            guess = player.guess(self._num_slots)

            if not self._is_easy_mode:
                # check duplicate numbers
                if len(set(guess)) != self._num_slots:
                    print("You cannot have duplicate numbers in normal mode")
                    continue

                # check numbers are within bounds
                if any(num < 1 or num > self._num_slots for num in guess):
                    print("You cannot guess random numbers in normal mode")
                    continue

            total_matching = self.calculate_score(guess)
            player.process_result(total_matching)

            if total_matching == self._num_slots:
                print(f"Congratulations, {player.name} won!")
                print(f"The correct answer was {self._correct_answer}.")
                print(f"{player.name} won in {self.round_number} guesses.")
                self.is_running = False
                return

    def calculate_score(self, guess: tuple[int, ...]) -> int:
        total_matching = 0
        for i in range(len(guess)):
            if guess[i] == self._correct_answer[i]:
                total_matching += 1

        return total_matching

