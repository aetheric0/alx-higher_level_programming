#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        return tuple((a, None))
    else:
        return tuple((a, sentence[0]))
