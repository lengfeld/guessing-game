#!/usr/bin/env python3

import sys
from random import randrange

def play():
    number = randrange(-10, 100)
    print("I have chosen a number.")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Error. You have not entered a number. Try again!")
            continue

        if guess < number:
            print("Your guess was to low!")
        elif guess > number:
            print("Your guess was to high!")
        else:
            print("Congrats. Your guess was correct.")
            break;


def main():
    while True:
        play()

        yes_or_no = input("Do you want to play again (y/n)?: ")
        if yes_or_no not in ('y', 'Y','yes','Yes','YES'):
                break

    return 0


if __name__ == '__main__':
    sys.exit(main())

