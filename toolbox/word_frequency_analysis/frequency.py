""" Analyzes the word frequencies in a book downloaded from
    Project Gutenberg """

import string
from pattern.web import URL
from os.path import exists

def get_word_list(file_name):
    """ Reads the specified project Gutenberg book.  Header comments,
            punctuation, and whitespace are stripped away.  The function
            returns a list of the words used in the book as a list.
            All words are converted to lower case.
    """

    if exists(file_name):
        fiel = open(file_name, 'r')
    else:
        with open(file_name, 'w') as fiel:
            page = URL('http://www.gutenberg.org/cache/epub/' + file_name[2:-4] + '/' + file_name)
            fiel.write(page.read().strip())
        fiel = open(file_name, 'r')

    txt = fiel.read()
    txt = txt[txt.index('*** START OF THIS PROJECT GUTENBERG EBOOK')
                        : txt.index('*** END OF THIS PROJECT GUTENBERG EBOOK')]
    for dot in string.punctuation:
        if dot is not "'":
            txt = txt.replace(dot, " ")
    txt = txt.lower()
    wordlist = txt.split()
    return wordlist


def get_top_n_words(word_list, n=100):
    """ Takes a list of words as input and returns a list of the n most frequently
            occurring words ordered from most to least frequently occurring.

            word_list: a list of words (assumed to all be in lower case with no
                                    punctuation
            n: the number of words to return
            returns: a list of n most frequently occurring words ordered from most
                             frequently to least frequentlyoccurring
            also nicely prints the list and the number of occurrences of each.
    """
    wordfreq = {}
    for word in word_list:
        if word in wordfreq:
            wordfreq[word] += 1
        else:
            wordfreq[word] = 1
    words = list(wordfreq.keys())
    numbers = list(wordfreq.values())
    if n > len(words):
        n = len(words)
    ordered = []
    for j in range(0, n):
        maxval = max(numbers)
        i = numbers.index(maxval)
        ordered.append(words.pop(i))
        print ordered[-1] + ' ' * (20 - len(ordered[-1])) + str(numbers[i])
        del(numbers[i])
    return ordered

wordlist = get_word_list('pg120.txt')
get_top_n_words(wordlist, 100)
