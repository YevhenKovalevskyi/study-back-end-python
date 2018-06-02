#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Вычисление факториала числа
"""

class Numbers:

    def factorial(self, n):
        return n * self.factorial(n - 1) if n else 1


if __name__ == "__main__":
    numObject = Numbers()
    for x in range(0, 10):
        print(numObject.factorial(x))
