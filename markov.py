from random import choice
# import sys
"""Generate Markov text from text files."""


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')
                                w1    w2   w3   w4  w5    w6

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words_list = text_string.split()

    index = 0
    while index < (len(words_list) - 2):
        # word = words_list[index]
        # next_word = words_list[index+1]
        # third_word = words_list[index+2]
        word, next_word, third_word = words_list[index:index+3]

        bigram = (word, next_word)

        if bigram in chains:
            chains[bigram].append(third_word)
        else:
            chains[bigram] = [third_word]

        # if bigram not in chains:
            # chains[bigram] = []
        # chains[bigram].append(third_word)

        # chains[bigram] = chains.get(bigram, []).append(third_word)

        index += 1

    last_tuple = (words_list[-2], words_list[-1])
    chains[last_tuple] = []

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    link = choice(list(chains.keys()))
    words.append(list(link))

    while chains[link]:
        next_word = choice(chains[link])
        words.append(next_word)
        link = (words[-2], words[-1])

    # print(words)

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
