import argparse
from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def counter(string) -> int:
    letters = Counter(string)
    return sum([letters[char] for char in letters if letters[char] == 1])


def main(*args):
    if len(args) > 0 and type(args[0]) == argparse.Namespace:
        arguments = args[0]
    else:
        arguments = create_parser().parse_args()

    if arguments.file:
        try:
            return get_string_from_file(arguments.file)
        except (PermissionError, FileExistsError, FileNotFoundError):
            return "File cannot be read"
    return counter(arguments.string)


def get_string_from_file(path):
    with open(path, "r") as f:
        return counter(f.read())


def create_parser():
    parsed = argparse.ArgumentParser()
    parsed.add_argument("--string")
    parsed.add_argument("--file")
    return parsed


if __name__ == "__main__":
    print(main())
