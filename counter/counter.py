def get_count(string) -> int:
    try:
        return archive[string]
    except KeyError:
        archive[string] = counter(string)
        return archive[string]


def counter(string) -> int:
    letters = {}
    output = 0
    for letter in string:
        try:
            letters[letter] += 1
        except KeyError:
            letters[letter] = 1
    for char in letters:
        if letters[char] == 1:
            output += 1
    return output


archive = {}
'''
while True:
    user_input = input("Input string: > ")
    exit() if user_input == '' else print(get_count(user_input))
'''