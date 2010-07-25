#!/usr/bin/env python

import string
import random

class Markov(object):

    """
    Markov-chain text generator. Translated
    from the original PHP into Python (haykranen.nl)
    """

    def __init__(self,text='alice.txt',length=600):
        fil = text
        fin = open('text/'+fil)
        self.text = ''
        forbid = '\\'
        for line in fin:
            self.text += line.translate(None,forbid).strip().lower()
        self.text_list = self.generate_markov_list(self.text)
        self.markov_table = self.generate_markov_table(self.text_list)
        self.length = length


    def _run(self):
        return self.generate_markov_text(self.length,self.markov_table)

    def generate_markov_list(self, text):
        return text.split()

    def generate_markov_table(self,text_list):
        self.table = {}

        # walk through text, make index table
        for i in range(len(self.text_list)-1):
            char = text_list[i]
            if char not in self.table:
                self.table[char] = {}

        # walk array again, count numbers
        for i in range(len(self.text_list)-1):

            char_index = self.text_list[i]
            char_count = self.text_list[i+1]

            if char_count not in self.table[char_index].keys():
                self.table[char_index][char_count] = 1
            else:
                self.table[char_index][char_count] += 1

        return self.table

    def generate_endings_list(self,text_list):
        pass

    def generate_markov_text(self, length, table):
        o = list()
        # get first character
        word = random.choice(table.keys())
        o.append(word)
        for i in range(length):
            newword = self.return_weighted_char(table[word])
            if newword:
                word = newword
                o.append(newword)
            else:
                word = random.choice(table.keys())
        return ' '.join(o)


    def return_weighted_char(self,array):
        if not array:
            return False
        else:
            total = sum(array.values())
            rand = random.randint(1,total)
            for key,value in array.iteritems():
                if rand <= value:
                    return key
                rand -= value


if __name__ == '__main__':
    import sys
    if sys.argv[1]:
        text = sys.argv[1]
    t = Markov(text)
    print t._run()
