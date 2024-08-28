#!/usr/bin/env python3

def return_evens(num_list):
   new_list = [n for n in num_list if n % 2 == 0]
   return new_list

print(return_evens([0, 1, 3, 5, 7, 8, 9]))    

def make_exclamation(sentence_list):
    # add an ! to a character if !. are missing
    # else if !. are present return the character as they are
    new_sentence = [char + '!' if char not in '!.' else char for char in sentence_list]
    return new_sentence

print(make_exclamation("hell'o! my name is Bree."))

