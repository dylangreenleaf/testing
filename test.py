"""THIS IS A TEST."""


import sys


def simple_print(string):
    for word in string.split(' '):
        print(word)


if __name__ == "__main__":
    sentence = sys.argv[1]
    simple_print(sentence)
