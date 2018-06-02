#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сортировка выбором улучшает пузырьковую сортировку, совершая всего один обмен за каждый проход по списку.
Чтобы сделать это, она ищет наибольший элемент и помещает его на соответствующую позицию.
Как и для пузырьковой сортировки, после первого прохода самый большой элемент находится на правильном месте.
После второго - на своё место становится следующий наибольший элемент.
Процесс продолжается, требуя n−1 проход для сортировки n элементов, поскольку последний из них автоматически оказывается на своём месте.
"""

from algorithms import Algorithms


class SelectionSort(Algorithms):

    @Algorithms.timing
    def selection_sort(self, data=[]):
        if data:
            for i in range(len(data)):
                min = i

                for j in range(i + 1, len(data)):
                    min = j if (data[j] < data[min]) else min

                if min != i:
                    data[i], data[min] = data[min], data[i]

        return data


if __name__ == "__main__":
    sortData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    sortObject = SelectionSort()

    print(sortData)
    print(sortObject.selection_sort(sortData))
