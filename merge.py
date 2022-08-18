#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __author__ = "Renato Patron"
    __license__ = "GPL"
    __version__ = "0.1"
    __maintainer__ = "Jurelex"
    __email__ = "jurelex@outlook.com"
    __status__ = "Production`
"""
# Imports

import itertools

# Creates out1.txt and out2.txt files after deleting any blank lines in the front.txt and back.txt files.
open('out1.txt','w').write(
    ''.join(
        l for l in open(
            'front.txt') if l.strip())) 
open('out2.txt','w').write(
    ''.join(
        l for l in open(
            'back.txt') if l.strip())) 

# Creates deck1.txt and deck2.txt.

f_1 = open("out1.txt", "r")
with open("deck1.txt", "w") as w:
    for x in f_1:
        # Stores the amount of times a card is included in the deck
        times = int(x[0:2])
        # Stores the name of the card
        card = x[2:]
        # Cleans the card name, by replacing the comma for a blank space
        clean_card = card.replace(",", " ")
        # outputs the card name
        while times > 0:
            w.write(f'"{clean_card.strip()}"\n')
            times -=1
            
f_2 = open("out2.txt", "r")
with open("deck2.txt", "w") as w:
    for x in f_2:
        # Stores the amount of times a card is included in the deck
        times = int(x[0:2])
         # Stores the name of the card
        card = x[2:]
        # Cleans the card name, by replacing the comma for a blank space
        clean_card = card.replace(",", " ")
        # outputs the card name
        while times > 0:
            w.write(f'"{clean_card.strip()}"\n')
            times -=1

# Uses the deck1.txt and deck2.txt files and merges them as a CSV file following the template in 
# https://mpcfill.com/static/cardpicker/template.9e9a90cf46aa.csv
filenames = ['deck1.txt', 'deck2.txt']

with open('deck1.txt') as src1, open('deck2.txt', 'r') as src2, open('merged.csv', 'w') as dst:
    dst.write(f"Quantity, Front, Back\n")
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(f"1, {line_from_first.strip()}, {line_from_second.strip()}\n")