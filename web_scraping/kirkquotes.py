"""
This program is a companion program to spockquotes.py. It scrapes IMDB for quotes from
Captain Kirk  in Star Trek, and uses natural language processing to analyze the sentiment
and objectivity of those quotes.

Run get_html the first time you run the program.
"""

from pattern.en import *
from pattern.web import *
import matplotlib.pyplot as plt


def get_html():
    """
    Connects to IMDB to obtain Kirk quotes and saves the HTML result in a file locally
    """
    imdbhtml = URL('http://www.imdb.com/character/ch0001448/quotes').download()
    imdbfile = open('imdbfilekirk', 'w')
    imdbfile.write(imdbhtml)
    imdbfile.close()
    print imdbhtml


def get_quotes():
    """
    Searches the file made by get_html for quotes from Kirk.
    Returns one set of quotes from Captain Kirk, as a list of strings.
    """
    with open('imdbfilekirk', 'r') as myfile:
        imdbhtml = myfile.read()
    quotes = []
    quotes2 = []
    quotes3 = []
    quote = False
    current = ''

    i = 0
    quote3 = False
    current = ''
    while i <= len(imdbhtml) - 1:
        # makes a list of kirk quotes
        character = imdbhtml[i]
        if imdbhtml[i:i + 52] == '<i><a href="/name/nm1517976/">James T. Kirk</a></i>:':
            quote3 = True
            quotes3.append(current)
            current = ''
            i += 55
        elif imdbhtml[i:i + 45] == '<i><a href="/name/nm0000638/">Kirk</a></i>:':
            quote3 = True
            quotes3.append(current)
            current = ''
            i += 48
        elif imdbhtml[i:i + 60] == '<i><a href="/name/nm0586003/">Captain James T. Kirk</a></i>:':
            quote3 = True
            quotes3.append(current)
            current = ''
            i += 63
        elif imdbhtml[i:i + 60] == '<i><a href="/name/nm0000638/">Captain James T. Kirk</a></i>:':
            quote3 = True
            quotes3.append(current)
            current = ''
            i += 63
        else:
            if character == '<':
                quote3 = False
                i += 1
            else:
                if quote3:
                    current += character
                    i += 1
                if quote3 == False:
                    i += 1
    quotes3.append(current)

    return {'Kirk': quotes3}


def graph(list1):
    """
    Takes input in the form of one list of strings one to several sentences in length,
    and graphs each on the axes of sentiment and subjectivity.
    """
    for element in list1:
        sens = sentiment(element)
        plt.plot([sens[0]], [sens[1]], 'ro')
        plt.xlabel('sentiment polarity')
        plt.ylabel('subjectivity')

    plt.show()


if __name__ == "__main__":
    # get_html()
    data = get_quotes()
    kirk = data['Kirk']
    graph(kirk)
