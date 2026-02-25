"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see:
# https://en.wikipedia.org/wiki/Magic_number_(programming)),
# you should define a PREPARATION_TIME constant
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(numbers_of_layers):
    """
    Indicate the preparation time required to make each layer of lasagna.

    :param PREPARATION_TIME: int - indicates the minutes it takes to make a layer of lasagna
    :param number_of_layer: int - indicates the number of layers the lasagna will have
    :return: PREPARATION_TIME * numbers_of_layers Indicating the total time to prepare all the 
    layers of the lasagna before baking it.
    """
    return numbers_of_layers * PREPARATION_TIME

#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(elapsed_bake_time, number_of_layers):
    """
    This function indicates the total time that has passed since the 
    lasagna was prepared and baked until now.
    :param elapsed_bake_time: int - indicates how long the lasagna has been baked
    :param number_of_layer: int Indicate the argument to be used in the function to 
        calculate the amount of time it took to prepare the lasagna.
    :time_per_layer: int - Take the value of the result of the function preparation_time_in_minutes
        with number_of_layers as an argument.
    :return: time_per_layer + elapsed_bake_time
    """
    time_per_layer = preparation_time_in_minutes(number_of_layers)
    return time_per_layer + elapsed_bake_time


#TODO: Remember to go back and add docstrings to all your functions
#(you can copy and then alter the one from bake_time_remaining.)
