import random


def main():
    num_slots = int(input("Enter number of slots (3 - 7): "))
    if num_slots <= 0:
        print(f"You can't guess {num_slots} numbers...")
        return
    elif num_slots < 3:
        print("That's too easy!")
        return
    elif num_slots > 7:
        print("Trust me that will take too long :)")
        return

    possible_numbers = list(range(1, num_slots + 1))
    random.shuffle(possible_numbers)
    correct_answer = tuple(possible_numbers)

    game_still_running = True
    while game_still_running:

        guess = input(f"Guess a permutation of 1-{num_slots}: ").split()
        if len(guess) != num_slots:
            print(f"You need to guess {num_slots} numbers!")
            continue

        guess = tuple(map(int, guess))

        total_matching = 0
        for i in range(len(guess)):
            if guess[i] == correct_answer[i]:
                total_matching += 1

        print(f"You got {total_matching} correct positions!")
        if total_matching == num_slots:
            print("Congratulations! You win.")
            print(f"The correct answer was {correct_answer}")
            game_still_running = False


if __name__ == "__main__":
    main()
