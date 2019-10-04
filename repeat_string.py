"""
Solution for first task of second homework
"""

import sys
from builtins import print


def pref_func(string):
    """See http://www.e-maxx-ru.1gb.ru/algo/prefix_function"""

    pref_f = [0] * len(string)
    for i in range(1, len(string)):
        j = pref_f[i-1]
        while j > 0 and string[i] != string[j]:
            j = pref_f[j-1]

        if string[i] == string[j]:
            j += 1
        pref_f[i] = j
    return pref_f


def main():
    """Just a main function"""

    string = input("Please provide a string: ")
    if not string:
        print("I can't work with empty string")

    pref_f = pref_func(string)
    # see http://www.e-maxx-ru.1gb.ru/algo/prefix_function
    potential_block_size = len(string) - pref_f[len(string)-1]
    result = len(string)
    if len(string) % potential_block_size == 0:
        result = potential_block_size

    print(len(string)/result)
    return 0


if __name__ == '__main__':
    sys.exit(main())
