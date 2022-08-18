#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    __author__ = "Renato Patron"
    __license__ = "GPL"
    __version__ = "0.2"
    __maintainer__ = "Jurelex"
    __email__ = "jurelex@outlook.com"
    __status__ = "Production"
    changelog:
        0.2 = Added a new feature: merging multiple decks for front and back cards. Decklist can be added directly to 
        the front_decks and back_decks folders. Also created a temp folder to keep temporary files in one place.
    
"""
# Imports

import glob
import itertools
import shutil

# Merges deckfiles in front_decks directory
with open("temp/front.txt", 'wb') as outfile:
    for filename in glob.glob('front_decks/*.txt'):
        if filename == "front.txt":
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
            
# Merges deckfiles in back_decks directory
with open("temp/back.txt", 'wb') as outfile:
    for filename in glob.glob('back_decks/*.txt'):
        if filename == "back.txt":
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)

# Creates out1.txt and out2.txt files after deleting any blank lines in the front.txt and back.txt files.
open('temp/out1.txt','w').write(
    ''.join(
        l for l in open(
            'temp/front.txt') if l.strip())) 
open('temp/out2.txt','w').write(
    ''.join(
        l for l in open(
            'temp/back.txt') if l.strip())) 

# Creates deck1.txt and deck2.txt.

f_1 = open("temp/out1.txt", "r")
with open("temp/deck1.txt", "w") as w:
    for x in f_1:
        # Stores the amount of times a card is included in the deck
        #times = int(x[0:2])
        # Stores the name of the card
        #card = x[2:]
        # For cube,no number provided
        card = x
        # Cleans the card name, by replacing the comma for a blank space
        clean_card = card.replace(",", " ")
        # outputs the card name
        #while times > 0:
        w.write(f'"{clean_card.strip()}"\n')
            #times -=1
            
f_2 = open("temp/out2.txt", "r")
with open("temp/deck2.txt", "w") as w:
    for x in f_2:
        # Stores the amount of times a card is included in the deck
        #times = int(x[0:2])
         # Stores the name of the card
        #card = x[2:]
        card = x
        # Cleans the card name, by replacing the comma for a blank space
        clean_card = card.replace(",", " ")
        # outputs the card name
        #while times > 0:
        w.write(f'"{clean_card.strip()}"\n')
            #times -=1

# Uses the deck1.txt and deck2.txt files and merges them as a CSV file following the template in 
# https://mpcfill.com/static/cardpicker/template.9e9a90cf46aa.csv
filenames = ['temp/deck1.txt', 'temp/deck2.txt']
# Outputs CSV file in CSV folder
with open('temp/deck1.txt') as src1, open('temp/deck2.txt', 'r') as src2, open('CSV/merged.csv', 'w') as dst:
    dst.write(f"Quantity, Front, Back\n")
    for line_from_first, line_from_second in itertools.zip_longest(src1, src2):
        if line_from_first is not None:
            dst.write(f"1, {line_from_first.strip()}, {line_from_second.strip()}\n")