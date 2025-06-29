from player import Player


class HumanPlayer(Player):
    def __init__(self, name: str = ""):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def guess(self, num_slots) -> tuple[int, ...]:
        name = "Your" if self._name == "" else f"{self._name}'s"

        while True:
            guess = input(f"{name} turn! Guess a permutation of 1-{num_slots}: ").split()
            if len(guess) == num_slots and all(s.isdigit() for s in guess):
                return tuple(map(int, guess))

            print(f"Please enter exactly {num_slots} positive integers (space-separated).")

    def process_result(self, result: int) -> None:
        name = "You" if self._name == "" else self._name
        print(f"{name} got {result} correct positions!\n")
