#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Родительский класс для различных алгоритмов
"""

import time


class Algorithms:

    @staticmethod
    def timing(func):
        def wrap(*args):
            time_start = time.time()
            ret = func(*args)
            time_end = time.time()

            print('%s function took %0.5f ms' % (func.__name__, (time_end - time_start) * 1000.0))

            return ret

        return wrap
