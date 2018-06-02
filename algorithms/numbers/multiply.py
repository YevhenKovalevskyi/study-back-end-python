#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Умножение чисел через сложение
"""

class Numbers:

    def multiply(self, a, b):
        result = 0

        if b != 0:
            prefix = '-' if ((a < 0 or b < 0) and not (a < 0 and b < 0)) else ''
            a = abs(a)
            b = abs(b)
            result = prefix + str(a + int(self.multiply(a, b - 1)))

        return result


if __name__ == "__main__":
    numObject = Numbers()
    print(numObject.multiply(-12, 23))
