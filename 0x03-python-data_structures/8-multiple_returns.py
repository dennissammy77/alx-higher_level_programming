#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0]
    tuple_a = (length, first_char)
    print("Length: {:d} - First character: {}".format(length, first_char))

sentence = "At school, I learnt C!"
multiple_returns(sentence)
