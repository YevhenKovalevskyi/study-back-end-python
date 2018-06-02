#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сортировка слиянием. Это рекурсивный алгоритм, который постоянно разбивает список пополам.
Если список пуст или состоит из одного элемента, то он отсортирован по определению (базовый случай).
Если в списке больше, чем один элемент, мы разбиваем его и рекурсивно вызываем сортировку слиянием для каждой из половин.
После того, как обе они уже отсортированы, выполняется основная операция, называемая слиянием.
Слияние - это процесс комбинирования двух меньших сортированных списков в один новый, но тоже отсортированный.
"""


class MergeSort:

    def merge_sort(self, data=[]):
        print("Splitting ", data)

        if len(data) > 1:
            delim = len(data) // 2
            ldata = data[:delim]
            rdata = data[delim:]

            self.merge_sort(ldata)
            self.merge_sort(rdata)

            i = 0
            j = 0
            k = 0

            while i < len(ldata) and j < len(rdata):
                if ldata[i] < rdata[j]:
                    data[k] = ldata[i]
                    i = i + 1
                else:
                    data[k] = rdata[j]
                    j = j + 1

                k = k + 1

            while i < len(ldata):
                data[k] = ldata[i]
                i = i + 1
                k = k + 1

            while j < len(rdata):
                data[k] = rdata[j]
                j = j + 1
                k = k + 1

            print("Merging ", data)
            #return data

if __name__ == "__main__":
    sortData = [3, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72, 6, 7]
    sortObject = MergeSort()

    print(sortData)
    print(sortObject.merge_sort(sortData))
