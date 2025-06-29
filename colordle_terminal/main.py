import random
from human_player import HumanPlayer
from simple_bot import SimpleBot


def main():
    human = HumanPlayer()
    bot = SimpleBot("Bot 1")

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

    num_guesses = 0

    game_still_running = True
    while game_still_running:
        num_guesses += 1

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

        human.process_result(total_matching)
        if total_matching == num_slots:
            print("Congratulations! You win.")
            print(f"The correct answer was {correct_answer}")
            print(f"You won in {num_guesses} guesses.")
            return

        # construct bot guess
        bot_guess = bot.guess(num_slots)

        bot_total_matching = 0
        for i in range(len(bot_guess)):
            if bot_guess[i] == correct_answer[i]:
                bot_total_matching += 1

        bot.process_result(bot_total_matching)
        if bot_total_matching == num_slots:
            print("The bot wins!")
            print(f"The correct answer was {correct_answer}")
            print(f"The bot took {num_guesses} guesses.")
            return


if __name__ == "__main__":
    main()
