#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ханойская башня
Три стержня и стопка дисков, каждый из которых немного меньше предыдущего.
Требуется переставить все диски с одного стержня на другой, соблюдая два строгих условия.
Во-первых, за раз можно было перемещать только один диск. Во-вторых, нельзя класть бОльший диск поверх меньшего.
"""

class Hanoi:

    def hanoi(self, plates, _from, to):
        while plates > 0:
            using = 6 - (_from + to)
            plates -= 1
            self.hanoi(plates, _from, using)
            print('Move plate ' + str(_from) + '->' + str(to))
            _from = using


if __name__ == "__main__":
    recObject = Hanoi()
    print(recObject.hanoi(5, 1, 3))
