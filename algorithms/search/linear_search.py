#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Линейный, последовательный поиск — алгоритм нахождения заданного значения произвольной функции на некотором отрезке.
Данный алгоритм является простейшим алгоритмом поиска и в отличие,
например, от двоичного поиска, не накладывает никаких ограничений на функцию и имеет простейшую реализацию.
Поиск значения функции осуществляется простым сравнением очередного рассматриваемого значения
(как правило поиск происходит слева направо, то есть от меньших значений аргумента к большим) и,
если значения совпадают (с той или иной точностью), то поиск считается завершённым.
"""

from algorithms import Algorithms


class LinearSearch(Algorithms):

    @Algorithms.timing
    def linear_search(self, data=[], s_val=0):
        if data:
            for i in range(0, len(data)):
                if s_val == data[i]:
                    return 'key: ' + str(i)

        return None


if __name__ == "__main__":
    listData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    searchObject = LinearSearch()

    print(listData)
    # x = int(input('Введите искомый элемент: '))
    print(searchObject.linear_search(listData, 72))

