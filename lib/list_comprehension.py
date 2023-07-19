#!/usr/bin/env python3

def return_evens(num_list):
    new_num_list = []
    i=0
    while i < len(num_list):
        if (num_list[i]%2 == 0):
            new_num_list.append(num_list[i])
        i += 1
    return new_num_list

def make_exclamation(sentence_list):
    i=0
    while i < len(sentence_list):
        sentence_list[i] += "!"
        i += 1
    return sentence_list