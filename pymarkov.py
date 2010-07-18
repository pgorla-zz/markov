#!/usr/bin/env python

import random

def generate_markov_table(text, look_forward):

    table = {}

    # walk through text, make index table
    for i in range(len(text)):
        char = text[i:look_forward]
        if char not in table:
            table[char] = {}
    print table

    # walk array again, count numbers
    for i in range(len(text) - look_forward):
        char_index = text[i:look_forward]
        char_count = text[i+look_forward:look_forward]

        if not char_count in table[char_index].keys():
            table[char_index][char_count] = 1
        else:
            table[char_index][char_count] += 1

    return table


def generate_markov_text(length, table, look_forward):
    # get first character
    char = random.choice(table.keys())
    o = char

    for i in range(length/look_forward):
        li_nums = []
        for k,v in table[char]:
            li_nums.append(v)

        newchar = return_weighted_char(table[char])

        if newchar:
            char = newchar
            o = newchar
        else:
            char = random.choice(table.keys())

    return o


def return_weighted_char(array):
    if not array:
        return False
    else:
        total = sum(array)
        rand = random.randint(1,total)
    for weight in array:
        if rand <= weight:
            return weight
            rand -= weight
















if __name__ == '__main__':
    fin = open('text/alice.txt')
    text = ''
    for line in fin:
        text += line.strip()
    generate_markov_table(text, 4)







