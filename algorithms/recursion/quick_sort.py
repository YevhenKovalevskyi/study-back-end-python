#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Быстрая сортировка использует технику “разделяй и властвуй”, чтобы получить те же преимущества, что и сортировка слиянием,
но при этом не использовать дополнительное место.
Однако, ценой за это станет то, что список может не поделиться пополам, приводя к уменьшению производительности.
Сначала быстрая сортировка выбирает значение, которое называется опорным элементом.
Несмотря на то, что есть много способов выбрать его, мы будем просто использовать первое значение в списке.
Роль опорного элемента заключается в помощи при разбиении списка.
Позиция, на которой он окажется в итоговом сортированном списке, обычно называемая точкой разбиения,
будет использоваться для разделения списка при последующих вызовах быстрой сортировки.
"""


class QuickSort():

    def qiuck_sort(self, data=[], s=0, f=0):
        if data:
            for i in range(f + 1, len(data)):
                if data[i] < data[f]:
                    pos = (f - 1) if f > 0 else 0
                    data.insert(pos, data.pop(i))
                    f += 1

            start = (s + 1) if s == f else 0

            if s != len(data) - 1:
                print(start)
                self.qiuck_sort(data, start, start)

        return data

    def qiuck_sort1(self, data=[]):
        if data:
            current = data[0]
            lesser = self.qiuck_sort1([x for x in data[1:] if x < current])
            greater = self.qiuck_sort1([x for x in data[1:] if x >= current])
            data = lesser + [current] + greater

        return data

    def qiuck_sort2(self, data=[]):
        return self.qiuck_sort2([x for x in data[1:] if x < data[0]]) + [data[0]] + self.qiuck_sort2(
            [x for x in data[1:] if x >= data[0]])


if __name__ == "__main__":
    sortData = [13, 4, 2, 5, 45, 67, 21, 15, 24, 17, 1, 95, 18, 72]
    sortObject = QuickSort()

    print(sortData)
    print(sortObject.qiuck_sort1(sortData))

