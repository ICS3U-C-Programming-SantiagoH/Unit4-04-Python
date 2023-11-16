#!/usr/bin/env python3
# Created by: Santiago Hewett
# Created on: Nov 15, 2023
# This program will ask the user
# for a number and will check if it is not a integer
# and then tell the user if they guessed correctly using random number

import random


def main():
    # create generator for correct_guess
    correct_guess = random.randint(1, 9)

    while True:
        # Get the user guess
        print("This program will ask the user for a number between 1 and 9 and ")
        print("then it will display if they guessed correctly or not.")

        user_guess_string = input("Please enter your guess between 1 and 9: ")

        # initialize variable
        user_guess_int = None

        # Try-except statement
        try:
            user_guess_int = int(user_guess_string)

            if user_guess_int < 1 or user_guess_int > 9:
                # Message for user number outside the range [1, 9]
                print("\n{} is not between 1 and 9.".format(user_guess_int))
            else:
                # Check if the user guess is equal to the correct guess
                if user_guess_int != correct_guess:
                    # Display if the user is wrong
                    print("\n{} is not correct.".format(user_guess_int))
                else:
                    # User guessed correctly, break the loop
                    break
        except ValueError:
            # Catch ValueError if the input is not a valid integer
            print("\n{} is not an integer.".format(user_guess_string))

    print("\nCongratulations! {} is the correct guess.".format(user_guess_int))


if __name__ == "__main__":
    main()
