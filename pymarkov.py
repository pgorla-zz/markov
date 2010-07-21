#!/usr/bin/env python

import random

def generate_markov_table(text, look_forward):

    table = {}

    # walk through text, make index table
    for i in range(len(text)):
        char = text[i:i+look_forward]
        if char not in table:
            table[char] = {}

    # walk array again, count numbers
    for i in range(len(text) - look_forward):
        char_index = text[i:i+look_forward]
        char_count = text[i+look_forward:i+look_forward+look_forward]

        if char_count not in table[char_index].keys():
            table[char_index][char_count] = 1
        else:
            table[char_index][char_count] += 1

    return table


def generate_markov_text(length, table, look_forward):
    # get first character
    char = random.choice(table.keys())
    o = char
    for i in range(length/look_forward):
        newchar = return_weighted_char(table[char])
        if newchar:
            char = newchar
            o += newchar
        else:
            char = random.choice(table.keys())
    return o


def return_weighted_char(array):
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
    import string
    if sys.argv[1]:
        fil = sys.argv[1]
    else:
        fil = 'alice.txt'
    if sys.argv[2]:
        length = int(sys.argv[2])
    else:
        length = 600

    fin = open('text/'+fil)
    text = ''
    forbid = '\\'
    for line in fin:
        text += line.translate(None,forbid).strip()
    markov = generate_markov_table(text, 4)
    print generate_markov_text(length,markov,3)


