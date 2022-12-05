#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    tuple_a = (length, first_char)
    return tuple_a
sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
