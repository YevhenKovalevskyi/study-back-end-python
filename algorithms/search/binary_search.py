#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Бинарный поиск начинает проверять элементы с находящегося в середине.
Если это то, что нам нужно, - всё готово. Если нет, то можно использовать упорядоченную природу списка, исключив половину оставшихся элементов.
Когда искомое больше, чем находящийся по середине элемент, то из дальнейшего рассмотрения можно смело исключить “нижнюю” часть, содержащую меньшие величины.
Искомое значение (если оно есть в списке) будет находиться в “верхней” части.
"""

from algorithms import Algorithms


class BinarySearch(Algorithms):

    @Algorithms.timing
    def binary_search(self, data=[], s_val=0):
        if data:
            found_index = 0
            steps = 1

            while len(data) > 0:
                delim = len(data) // 2

                if s_val == data[delim]:
                    return 'key: ' + str(found_index + delim), 'step: ' + str(steps)
                elif s_val < data[delim]:
                    data = data[:delim]
                else:
                    found_index += delim
                    data = data[delim:]

                steps += 1

        return None


if __name__ == "__main__":
    listData = [x for x in range(0, 50)]
    searchObject = BinarySearch()

    print(listData)
    # x = int(input('Введите искомый элемент: '))
    print(searchObject.binary_search(listData, 1))

