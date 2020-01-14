#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A number (n) of lamps are placed in a line, some are switched on and some are off. Write a function that will return the smallest number of lamps that need to be switched on or off so that the line of lamps alternate.

https://dev.to/thepracticaldev/daily-challenge-149-fun-with-lamps-11nk
"""

def lamps(lamps_list):
    steps = 0
    for idx in range(0, len(lamps_list) - 1):
        if lamps_list[idx + 1] == lamps_list[idx]:
            steps += 1
            lamps_list[idx + 1] = 1 if lamps_list[idx] == 0 else 0
    return steps
if __name__ == "__main__":
    assert lamps([1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]) == 5
    assert lamps([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 6
    assert lamps([1, 0, 1]) == 0
    assert lamps([1, 0, 1, 0]) == 0
    assert lamps([0, 1, 0, 1, 0]) == 0
    assert lamps([1, 0, 1, 0, 0, 1, 0, 1]) == 4
    assert lamps([1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]) == 6
