from game_logo import logo, vs
from game_data import data
from utility_functions import *
import random

# current and next indexes will represent the current options displayed on screen.
# previous will represent the option that was just cleared off from the screen.
previous_index = -1
next_index = -1
score = 0

print(logo)

# data is a list of multiple dictionaries
current_index = random.randint(0, len(data) - 1)
option_B = data[current_index]

game_continue = True
while game_continue:

    # Option B will become Option A in each loop
    option_A = option_B
    next_index = random.randint(0, len(data) - 1)

    # next_index == current_index, will prevent option A and option B from being same
    # next_index == previous_index, will prevent next option B from being same as the previous option A
    while next_index == current_index or next_index == previous_index:
        next_index = random.randint(0, len(data) - 1)

    option_B = data[next_index]

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
        # Current index (Option A) will become previous index
        previous_index = current_index
        # Next index (Option B) will become Option A (current index)
        current_index = next_index
        # Next index becomes undefined. It will get value in the next loop
        next_index = -1
    else:
        game_continue = False
        print(f"\n{'+' * 40}")
        print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{'+' * 40}")
