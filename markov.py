#!/usr/bin/env python

import string
from random import randint

class Generate_Table():

    def __init__(self):
        self.filename = 'text/alice.txt'
        self.text = open(self.filename)
        self.fulltext = self.generate_fulltext()
        self.words_by_number = self.generate_word_list()

    def generate_fulltext(self):
        exclude = set(string.punctuation)
        text_ = ''
        for line in self.text:
            text_ += line.strip()
        # get rid of punctuation. TODO: add back in.
        text_ = ''.join(ch for ch in text_ if ch not in exclude)
# TODO
# generate_fulltext() currently churns out
# 'atPresent', 'to\xe3\mor\ehe\x..'
# fix?
        return text_.split()

    def generate_word_list(self):
        word_list_ = {}
        for word in self.fulltext:
            if not word_list_.has_key(word):
                word_list_[word] = 1
            else:
                word_list_[word] += 1
        return word_list_

    def couple(self):



# metadata? (authorship, which text used, etc)
# D = {}
# D[word] = count


class Word(Generate_Table):

    def __init__(self):


class Generate_Word_list(Generate_Table):
    def __init__(self):
        self.count = 0




"""
we need to calculate the
probabilities between each word. hm.
neural networks?
but now, focus on creating this thing.

Possibly working idea:

{
  'the'       : {0.9:'bear', 0.3:'Kool-Aid'},
  'peaches'   : {0.2:'palm', 0.4:'fence'}
  'stuff'     : {0.5:'bodies', 0.9:'turkey'}
}

{
  word_object : {P(following_word):following_word}
}
"""






if __name__ == '__main__':
    t = Generate_Table()
