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
    try:
        with open(path, "r") as f:
            return counter(f.read())
    except (PermissionError, FileExistsError, FileNotFoundError):
        return "File cannot be read"


def create_parser():
    parsed = argparse.ArgumentParser()
    parsed.add_argument("--string")
    parsed.add_argument("--file")
    return parsed


if __name__ == "__main__":
    args = create_parser()
    print(main(args.parse_args()))
