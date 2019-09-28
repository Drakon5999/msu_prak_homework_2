"""
Solution for second task of second homework
"""

import sys
from builtins import print
from collections import Counter


def get_most_popular_word(text):
    words = text.split()
    most_popular = Counter(words).most_common(2)
    if not most_popular or (len(most_popular) == 2 and most_popular[0][1] == most_popular[1][1]):
        return '—'
    return most_popular[0][0]


def main():
    """Just a main function"""

    txts = []
    txt = sys.stdin.readline()
    while txt.strip():
        txts.append(txt)
        txt = sys.stdin.readline()

    print(get_most_popular_word(' '.join(txts)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
