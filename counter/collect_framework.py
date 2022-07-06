import argparse
from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def counter(string) -> int:
    letters = Counter(string)
    return sum([letters[char] for char in letters if letters[char] == 1])


def main(arguments):
    if arguments.file:
        return get_string_from_file(arguments.file)
    return counter(arguments.string)


def get_string_from_file(path):
    with open(path, "r") as f:
        return counter(f.read())


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--string")
    argparse.add_argument("--file")
    args = argparse.parse_args()
    print(main(args))
