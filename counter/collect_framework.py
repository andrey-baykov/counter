import argparse
from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def counter(string) -> int:
    letters = Counter(string)
    return sum([letters[char] for char in letters if letters[char] == 1])


def main():
    arguments = create_parser()
    if arguments.file:
        try:
            output = get_string_from_file(arguments.file)
        except (PermissionError, FileExistsError, FileNotFoundError):
            output = "File cannot be read"
    else:
        output = counter(arguments.string)
    return output


def get_string_from_file(path):
    with open(path, "r") as f:
        return counter(f.read())


def create_parser():
    parsed = argparse.ArgumentParser()
    parsed.add_argument("--string")
    parsed.add_argument("--file")
    output = parsed.parse_args()
    return output


if __name__ == "__main__":
    print(main())
