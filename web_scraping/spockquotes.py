"""
This program scrapes IMDB for quotes from Spock in Star Trek, and uses natural language processing
to analyze the sentiment and objectivity of those quotes.

Run get_html the first time you run the program.
"""

from pattern.en import *
from pattern.web import *
import matplotlib.pyplot as plt


def get_html():
    """
    Connects to IMDB to obtain Spock quotes and saves the HTML result in a file locally
    """
    imdbhtml = URL('http://www.imdb.com/character/ch0001439/quotes').download()
    imdbfile = open('imdbfile', 'w')
    imdbfile.write(imdbhtml)
    imdbfile.close()
    # print imdbhtml


def get_quotes():
    """
    Searches the file made by get_html for quotes from Spock.
    Returns three sets of quotes: those from Spock in the new movies (played by Zachary Quinto), 
    those from Spock in all other continuities (played by Leonard Nimoy), and a small selection of 
    those from Kirk for comparison.
    """
    with open('imdbfile', 'r') as myfile:
        imdbhtml = myfile.read()

    quotes = []
    quotes2 = []
    quotes3 = []
    quote = False
    current = ''
    i = 0

    while i <= len(imdbhtml) - 1:
        # makes a list of original spock quotes
        character = imdbhtml[i]
        if imdbhtml[i: i + 44] == '<i><a href="/name/nm0000559/">Spock</a></i>:':
            quote = True
            quotes.append(current)
            current = ''
            i += 47
        elif imdbhtml[i:i + 48] == '<i><a href="/name/nm0000559/">Mr. Spock</a></i>:':
            quote = True
            quotes.append(current)
            current = ''
            i += 51
        elif imdbhtml[i:i + 52] == '<i><a href="/name/nm0000559/">Captain Spock</a></i>:':
            quote = True
            quotes.append(current)
            current = ''
            i += 55
        else:
            if character == '<':
                quote = False
                i += 1
            else:
                if quote == True:
                    current += character
                    i += 1
                if quote == False:
                    i += 1
    quotes.append(current)

    i = 0
    quote2 = False
    current = ''
    while i <= len(imdbhtml) - 1:
        # makes a list of new spock quotes
        character = imdbhtml[i]
        if imdbhtml[i:i + 44] == '<i><a href="/name/nm0704270/">Spock</a></i>:':
            quote2 = True
            quotes2.append(current)
            current = ''
            i += 47
        else:
            if character == '<':
                quote2 = False
                i += 1
            else:
                if quote2:
                    current += character
                    i += 1
                if quote2 == False:
                    i += 1
    quotes2.append(current)

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

    return {'OldSpock': quotes, 'NewSpock': quotes2, 'Kirk': quotes3}


def graph(list1, list2, list3):
    """
    Takes input in the form of three lists of strings one to several sentences in length,
    and graphs each on the axes of sentiment and subjectivity.
    """
    for element in list1:
        sens = sentiment(element)
        plt.plot([sens[0]], [sens[1]], 'go')
        plt.xlabel('sentiment polarity')
        plt.ylabel('subjectivity')
    for element in list2:
        sens = sentiment(element)
        plt.plot([sens[0]], [sens[1]], 'bo')
        plt.xlabel('sentiment polarity')
        plt.ylabel('subjectivity')
    for element in list3:
        sens = sentiment(element)
        plt.plot([sens[0]], [sens[1]], 'ro')
        plt.xlabel('sentiment polarity')
        plt.ylabel('subjectivity')
    plt.show()


if __name__ == "__main__":
    #get_html()
    data = get_quotes()
    old = data['OldSpock']
    new = data['NewSpock']
    kirk = data['Kirk']
    graph(old, new, kirk)
