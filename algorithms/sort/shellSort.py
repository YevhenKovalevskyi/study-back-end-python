#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сортировку Шелла иногда называют “сортировкой с уменьшением инкремента”.
Она улучшает сортировку вставками, разбивая первоначальный список на несколько подсписков, каждый из которых сортируется по отдельности.
Оригинальный способ выбора таких подсписков - ключевая идея сортировки Шелла.
Вместо того, чтобы выделять подсписки из стоящих рядом элементов, сортировка Шелла использует инкремент i (приращение),
чтобы создавать подсписки из значений, отстоящих на расстоянии i друг от друга.
"""

from algorithms import Algorithms


class ShellSort(Algorithms):

    @Algorithms.timing
    def shell_sort(self, data=[]):
        if data:
            d = int(len(data) / 2)

            while d > 0:
                for i in range(1, len(data), d):
                    for j in range(0, i, d):
                        if data[i] < data[j]:
                            data[i], data[j] = data[j], data[i]

                d = int(d / 2)

        return data


if __name__ == "__main__":
    sortData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    sortObject = ShellSort()

    print(sortData)
    print(sortObject.shell_sort(sortData))
