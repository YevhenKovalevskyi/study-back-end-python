#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сортировка вставками, имея по-прежнему O(n2), работает несколько иначе.
Она всегда поддерживает в сортированном виде подсписок на нижних индексах списка.
Каждый новый элемент “вставляется” в упорядоченный на прошлой итерации подсписок так, чтобы тот остался сортированным и стал на один элемент больше.
"""

from algorithms import Algorithms


class InsertSort(Algorithms):

    @Algorithms.timing
    def insert_sort(self, data=[]):
        if data:
            for i in range(1, len(data)):
                for j in range(0, i):
                    if data[i] < data[j]:
                        data[i], data[j] = data[j], data[i]

        return data


if __name__ == "__main__":
    sortData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    sortObject = InsertSort()

    print(sortData)
    print(sortObject.insert_sort(sortData))

