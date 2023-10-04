#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i, j in enumerate(str):
        if i != n:
            new += j
            return new
