#!/usr/bin/env python3

def return_evens(num_list):
   new_list = [n for n in num_list if n % 2 == 0]
   return new_list

print(return_evens([0, 1, 3, 5, 7, 8, 9]))    

def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]  

print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))
