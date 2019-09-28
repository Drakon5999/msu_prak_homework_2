"""
Solution for third task of second homework
"""

import sys
from builtins import print
import itertools

DIGIT_TO_LETTERS = {
    "1": "-",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
    "0": " ",
}


def main():
    """Just a main function"""
    number = input("Please provide a number: ").strip()
    lists = []
    for digit in number:
        if digit in DIGIT_TO_LETTERS:
            lists.append(DIGIT_TO_LETTERS[digit])
        else:
            print("Bad digit {}".format(digit))
            return 1

    print([''.join(element) for element in itertools.product(*lists)])
    return 0


if __name__ == '__main__':
    sys.exit(main())
