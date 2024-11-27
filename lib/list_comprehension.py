#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [n for n in num_list if n % 2 ==0]
    return(even_num)


def make_exclamation(sentence_list):
    exclaimed_sentence = []
    for sentence in sentence_list:
        exclaimed_sentence.append(sentence + '!')

    return(exclaimed_sentence)





   