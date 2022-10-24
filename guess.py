#!/usr/bin/env python3

import sys
from random import randrange

def play():
    number = randrange(0, 10)
    print("I have chosen a nomber.")

    while True:
        try:
            guess = int(input("Your guesss: "))
        except ValueError:
            print("Error. You have not entered a number. Try again!")
            continue

        if guess < number:
            print("Your guess was to low!")
        elif guess > number:
            print("Your guess was to high!")
        else:
            print("Congratulations. Your guess was correct.")
            break;


def main():
    while True:
        play()

        yes_or_no = input("Do you want to play again (y/n)?: ")
        if yes_or_no not in ('y', 'Y'):
                break

    return 0


if __name__ == '__main__':
    sys.exit(main())
