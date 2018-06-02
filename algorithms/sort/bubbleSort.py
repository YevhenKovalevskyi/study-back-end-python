#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Пузырьковая сортировка состоит в повторяющихся проходах по сортируемому массиву.
За каждый проход элементы последовательно сравниваются попарно и, если порядок в паре неверный, выполняется обмен элементов.
Проходы по массиву повторяются до тех пор, пока на очередном проходе не окажется, что обмены больше не нужны, что означает — массив отсортирован.
При проходе алгоритма, элемент, стоящий не на своём месте, «всплывает» до нужной позиции как пузырёк в воде, отсюда и название алгоритма.
Для понимания и реализации этот алгоритм — простейший, но эффективен он лишь для небольших массивов. Сложность алгоритма: O(n²).
"""

from algorithms import Algorithms


class BubbleSort(Algorithms):

    @Algorithms.timing
    def bubble_sort(self, data=[]):
        if data:
            for i in range(len(data)):
                for j in range(i + 1, len(data)):
                    if data[i] > data[j]:
                        data[i], data[j] = data[j], data[i]

        return data


if __name__ == "__main__":
    sortData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    sortObject = BubbleSort()

    print(sortData)
    print(sortObject.bubble_sort(sortData))
