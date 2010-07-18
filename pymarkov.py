#!/usr/bin/env python

from random import randint


def generate_markov_table(text, look_forward):

    table = []

    # walk through text, make index table
    for i in range(len(text)):
        char = text[i:look_forward]
        if not char in table:
            table[char] = []

    # walk array again, count numbers
    for i in range(len(text) - look_forward):
        char_index = text[i:look_forward]
        char_count = text[i+look_forward:look_forward]

        if table[char_index][char_count]:
            table[char_index][char_count] += 1
        else:
            table[char_index][char_count] = 1

    return table


def generate_markov_text(length, table, look_forward):
    # get first character
    char = table[randint(0,len(table))]
    o = char

    for i in range(length/look_forward):
        newchar = return_weighted_char(table[char])

        if newchar:
            char = newchar
            o = newchar
        else:
            char = table[randint(0,len(table))]

    return o


def return_weighted_char(array):
    if not array:
        return False
    else:
        total = sum(array)
        rand = randint(1,total)
    for weight in array:
        if rand <= weight:
            return weight
            rand -= weight























