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
            self.text += line.translate(None,forbid).strip()
        self.markov_table = self.generate_markov_table(self.text, 3)
        self.length = length


    def _run(self):

        return self.generate_markov_text(self.length,self.markov_table,3)


    def generate_markov_table(self, text, look_forward):
        self.table = {}

        # walk through text, make index table
        for i in range(len(self.text)):
            char = self.text[i:i+look_forward]
            if char not in self.table:
                self.table[char] = {}

        # walk array again, count numbers
        for i in range(len(self.text) - look_forward):
            char_index = self.text[i:i+look_forward]
            char_count = self.text[i+look_forward:i+look_forward+look_forward]

            if char_count not in self.table[char_index].keys():
                self.table[char_index][char_count] = 1
            else:
                self.table[char_index][char_count] += 1

        return self.table


    def generate_markov_text(self, length, table, look_forward):
        # get first character
        char = random.choice(table.keys())
        o = char
        for i in range(length/look_forward):
            newchar = self.return_weighted_char(table[char])
            if newchar:
                char = newchar
                o += newchar
            else:
                char = random.choice(table.keys())
        return o


    def return_weighted_char(self,array):
        if not array:
            return False
        else:
            total = sum(array.values())
            rand = random.randint(1,total)
            for k,v in array.iteritems():
                if rand <= v:
                    return k
                rand -= v


if __name__ == '__main__':
    import sys
    if sys.argv[1]:
        text = sys.argv[1]
    t = Markov(text)
    print t._run()
