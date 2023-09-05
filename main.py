from game_logo import logo, vs
from utility_functions import *

print(logo)
score = 0
options_index_list = []
previous_index = -1

game_continue = True
while game_continue:
    options_index_list = select_two_random_index_from_data(options_index_list, previous_index)

    index = options_index_list[0]
    option_A = get_values(index)
    print(f"\nCompare A: {option_A[0]}, {option_A[1]}, from {option_A[2]}.")
    index = options_index_list[1]
    option_B = get_values(index)
    print(vs)
    print(f"\nAgainst B: {option_B[0]}, {option_B[1]}, from {option_B[2]}.")
    user_guess = input("\nWho has more Instagram followers? Type 'A' or 'B' :").upper()

    correct_ans = "A" if option_A[3] > option_B[3] else "B"

    if user_guess == correct_ans:
        score += 1
        clear_screen()
        print(f"\n{'-' * 40}")
        print(f"You're right! Current Score: {score}")
        print(f"{'-' * 40}")
        # second option will become first option
        previous_index = options_index_list[0]
        options_index_list.remove(previous_index)
        option_A = option_B
    else:
        game_continue = False
        print(f"\n{'+' * 40}")
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{'+' * 40}")
