from itertools import permutations


words = None


def load_words():
    file = open("words_alpha.txt")
    # It shocks me that python can read this in a reasonable amount of time
    text = file.read()

    all_words = text.split("\n")

    global words

    # Use of a set is practically cheating
    words = set()

    for word in all_words:
        if len(word) > 2:
            words.add(word)


def get_possibilities(letters):
    global words

    possible_words = []

    # Ensure the words are loaded
    if words is None:
        load_words()

    # The number of possible words is very low, as there are few letters
    for i in range(len(letters)):
        for test_word in permutations(letters, i):
            print(test_word)
            if test_word in words:
                possible_words.append(test_word)

    return possible_words
