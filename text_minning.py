####### Python 3.6
####### author: Rafael Calixto
####### created at: 08/25/2018
####### description: This library contains objects to process the text of the
####### crawled web page.

from re import findall
from collections import Counter
from nltk import word_tokenize, pos_tag

class Minner:
    ''' This object returns all the content between the tags p
        in the html code.'''
    def dig(html):
        ### input str {html code}
        ### output str {page text}
        site_text = ''
        for each_p in findall(r'<p>(.*?)</p>', html):
            site_text += each_p + '\n'
        return site_text

class Word_count:
    ''' This object provides the frequency of each word in the text.'''
    def count(text):
        ### input str
        ### output dict
        return dict(Counter(text.lower().split()))

class Word_classifier:
    ''' This object provides the gramatical class of each word in the text.'''
    def classify(text):
        ### input str
        ### output list {taged tokens}
        return pos_tag(word_tokenize(text.lower()))
