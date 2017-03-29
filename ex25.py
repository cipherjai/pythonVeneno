# inbuilt functions


def break_words(stuff):
    """This would break the words"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words"""
    return sorted(words)


def print_first_word(words):
    """ Takes the first word after popping it """
    word = words.pop(0)
    return word


def print_last_word(words):
    """ Takes the last word after popping it """
    word = words.pop(-1)
    return word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words()


def print_first_and_last(sentence):
    """Prints the last and forst """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


