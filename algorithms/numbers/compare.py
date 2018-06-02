#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сравнение чисел
"""

class Numbers:

    def compare(self, a, b):
        return int(abs((a + b) / 2.) - abs((a - b) / 2.))


if __name__ == "__main__":
    numObject = Numbers()
    print(numObject.compare(-12, 23))
