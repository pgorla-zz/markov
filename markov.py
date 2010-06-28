#!/usr/bin/python

import string

class Generate_Table():

    """Generate Markov table from input text."""

    def __init__(self):
        self.filename = 'alice.txt'
        self.text = open(self.filename)
        self.fulltext = self.generate_fulltext()

    def generate_fulltext(self):
        exclude = set(string.punctuation)
        text_ = ''
        for line in self.text:
            text_ += line.strip()
        text_ = ''.join(ch for ch in text_ if ch not in exclude)
        return text_.split()

    def generate_word_list(self):
        word_list_ = {}
        for word in self.fulltext:
            if not word_list_.has_key(word):
                word_list_[word] = 1
            else:
                word_list_[word] += 1
        return word_list_

# metadata? (authorship, which text used, etc)
# D = {}
# D[word] = count

class Word(Generate_Table):
    def __init__(self):
        pass

class Generate_Word_list(Generate_Table):
    def __init__(self):
        self.count = 0

# we need to calculate the
# probabilities between each word. hm.
# neural networks?
# but now, focus on creating this thing.


if __name__ == '__main__':
    t = Generate_Table()
