from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def counter(string) -> int:
    letters = Counter(string)
    return sum([letters[char] for char in letters if letters[char] == 1])


def main(arguments):
    if arguments.file_path:
        with open(arguments.file_path, "r") as file:
            return counter(file.read())
    return counter(arguments.string)
