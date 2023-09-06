from game_logo import logo, vs
from game_data import data
from utility_functions import *
import random

score = 0
print(logo)

# data is a list of multiple dictionaries
previous_option = None
option_B = random.choice(data)

game_continue = True
while game_continue:

    # Option B will become Option A in each loop
    option_A = option_B

    # option_B == option_A, will prevent option B and option A from being same
    # option_B == previous_option, will prevent next option B from being same as the previous option A
    while option_B == option_A or option_B == previous_option:
        option_B = random.choice(data)

    print(f"\nCompare A: {option_A['name']}, {option_A['description']}, from {option_A['country']}.")
    print(vs)
    print(f"\nAgainst B: {option_B['name']}, {option_B['description']}, from {option_B['country']}.")

    user_guess = get_user_guess()
    correct_ans = "A" if option_A['follower_count'] > option_B['follower_count'] else "B"

    if user_guess == correct_ans:
        score += 1
        clear_screen()
        print(f"\n{'-' * 40}")
        print(f"You're right! Current Score: {score}")
        print(f"{'-' * 40}")
        # Option A will become previous index
        previous_option = option_A
    else:
        game_continue = False
        print(f"\n{'+' * 40}")
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{'+' * 40}")
