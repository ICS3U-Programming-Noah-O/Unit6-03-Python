#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 31, 2022
# This program find the min value in an array
# of random integers


import random
import constants


def calculate_min_value(rand_array):
    # This function calculates the min
    min_value = rand_array[0]
    # Loop that calculates the min value
    for num in (rand_array):
        if min_value > num:
            min_value = num
    # Return the min value
    return min_value


def main():
    # This function creates the array and
    # fills the array
    array = []
    for counter in range(10):
        num = random.randint(constants.MIN, constants.MAX)

        array.append(num)
        print("{} added in position {}.".format(num, counter))
    min_v = calculate_min_value(array)
    print(array)
    print(" ")
    print("The minimum value is {}.".format(min_v))


if __name__ == "__main__":
    main()
