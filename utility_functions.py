import os
import random
from game_data import data


def clear_screen():
    """This function clears the console"""
    os.system('cls')


def select_two_random_index_from_data(options_index_list, previous_index):
    """This function randomly selects two indexes from data[] in game_data.py, append them in a list and returns that
    list. It takes two parameters - your current options index list and the previously removed index from the options
    index list."""
    while len(options_index_list) != 2:
        random_index = random.randint(0, len(data) - 1)
        if random_index not in options_index_list and random_index != previous_index:
            options_index_list.append(random_index)
    return options_index_list


def get_values(index_value):
    """This function fetches name, description, country and followers count values from data[] for a particular index
    and returns a list made from those values"""
    name = data[index_value]['name']
    description = data[index_value]['description']
    country = data[index_value]['country']
    followers_count = data[index_value]['follower_count']
    return [name, description, country, followers_count]
