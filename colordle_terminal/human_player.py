from player import Player


class HumanPlayer(Player):
    def __init__(self, name: str = ""):
        self.name = name

    def guess(self, num_slots) -> tuple[int, ...]:
        name = "Your" if self.name == "" else f"{self.name}'s"

        while True:
            guess = input(f"{name} turn! Guess a permutation of 1-{num_slots}: ").split()
            if len(guess) == num_slots and all(s.isdigit() for s in guess):
                return tuple(map(int, guess))

            print(f"Please enter exactly {num_slots} positive integers (space-separated).")

    def process_result(self, result: int) -> None:
        name = "You" if self.name == "" else self.name
        print(f"{name} got {result} correct positions!\n")
