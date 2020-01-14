#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Determine if a word is an isogram

An isogram is a word that has no repeating letters, consecutive or non-consecutive.

https://dev.to/thepracticaldev/daily-challenge-159-isogram-3h4

"""

def is_isogram(word):
    word = word.lower()
    return len(set(word)) == len(word)

assert is_isogram("Dermatoglyphics") == True
assert is_isogram("aba") == False