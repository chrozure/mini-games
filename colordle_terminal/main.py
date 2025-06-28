import random
from human_player import HumanPlayer


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

    is_easy_mode = False
    easy_mode_input = input("Would you like to play on easy mode? (y/n): ").lower()
    if easy_mode_input == 'y':
        is_easy_mode = True

    possible_numbers = list(range(1, num_slots + 1))
    random.shuffle(possible_numbers)
    correct_answer = tuple(possible_numbers)

    human = HumanPlayer()
    num_guesses = 0
    bot_guesses = []

    game_still_running = True
    while game_still_running:

        # get human guess
        guess = human.guess(num_slots)

        # check duplicate numbers
        if not is_easy_mode and len(set(guess)) != num_slots:
            print("You cannot have duplicate numbers in normal mode")
            continue

        # check numbers are in bound
        if not is_easy_mode and any(num < 1 or num > num_slots for num in guess):
            print("You cannot guess random numbers in normal mode")
            continue

        # calculate score
        total_matching = 0
        for i in range(len(guess)):
            if guess[i] == correct_answer[i]:
                total_matching += 1

        num_guesses += 1
        human.process_result(total_matching)
        if total_matching == num_slots:
            print("\nCongratulations! You win.")
            print(f"The correct answer was {correct_answer}")
            print(f"You won in {num_guesses} guesses.")
            return

        # construct bot guess
        # while True:
        #     random.shuffle(possible_numbers)
        #     bot_guess = tuple(possible_numbers)
        #
        #     if bot_guess not in bot_guesses:
        #         break
        #
        # bot_guesses.append(bot_guess)
        # bot_total_matching = 0
        # for i in range(len(bot_guess)):
        #     if bot_guess[i] == correct_answer[i]:
        #         bot_total_matching += 1
        #
        # print(f"The bot guessed {bot_guess}")
        # print(f"The bot got {bot_total_matching} positions correct")
        # if bot_total_matching == num_slots:
        #     print("The bot wins!")
        #     print(f"The correct answer was {correct_answer}")
        #     print(f"The bot took {len(bot_guesses)} guesses.")
        #     return


if __name__ == "__main__":
    main()
