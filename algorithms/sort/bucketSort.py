#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Блочная сортировка (Карманная сортировка, корзинная сортировка, англ. Bucket sort) — алгоритм сортировки,
в котором сортируемые элементы распределяются между конечным числом отдельных блоков (карманов, корзин) так,
чтобы все элементы в каждом следующем по порядку блоке были всегда больше (или меньше), чем в предыдущем.
Каждый блок затем сортируется отдельно, либо рекурсивно тем же методом, либо другим.
Затем элементы помещаются обратно в массив. Этот тип сортировки может обладать линейным временем исполнения O(N).
Данный алгоритм требует знаний о природе сортируемых данных, выходящих за рамки функций "сравнить" и "поменять местами",
достаточных для сортировки слиянием, сортировки пирамидой, быстрой сортировки, сортировки Шелла, сортировки вставкой.
Недостатки: сильно деградирует при большом количестве мало отличных элементов,
или же на неудачной функции получения номера корзины по содержимому элемента.
В некоторых таких случаях для строк, возникающих в реализациях основанного на сортировке строк алгоритма сжатия BWT,
оказывается, что быстрая сортировка строк в версии Седжвика значительно превосходит блочную сортировку скоростью.
"""

from algorithms import Algorithms


class BucketSort(Algorithms):

    def insert_sort(self, data=[]):
        if data:
            for i in range(1, len(data)):
                for j in range(0, i):
                    if data[i] < data[j]:
                        data[i], data[j] = data[j], data[i]

        return data

    @Algorithms.timing
    def bucket_sort(self, data=[]):
        new_data = []

        if data:
            buckets = {}
            sortedBucket = {}

            for value in data:
                b_key = str(value)[:1]
                buckets.setdefault(b_key, []).append(value)

            for key, value in buckets.items():
                sortedBucket[str(key)] = self.insert_sort(value)

            for i in range(0, 10):
                if str(i) in sortedBucket.keys():
                    new_data += sortedBucket.get(str(i))

        return new_data


if __name__ == "__main__":
    sortData = [312, 421, 218, 531, 452, 727, 215, 135, 224, 117, 109, 475, 162]
    sortObject = BucketSort()

    print(sortData)
    print(sortObject.bucket_sort(sortData))
