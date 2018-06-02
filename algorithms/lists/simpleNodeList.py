#!/usr/bin/env python
# -*- coding: utf-8 -*-

#класс Node для определения элемента списка
class Node:
    def __init__(self, value = '', next = ''):
        self.value = value
        self.next  = next
    #end def
#end class

class LinkedList:
    def __init__(self):
        self.first  = ''
        self.last   = ''
        self.length = 0
    #end def

    # очистка списка
    def clear(self):
        self.__init__()
    #end def

    # добавление элемента списка
    def add_item(self, x):
        self.length += 1

        if self.first == '':
            self.last = self.first = Node(x, '')
        else:
            self.last.next = self.last = Node(x, '')
    #end def

    # добавление кольцевого элемента списка
    def add_item_circle(self, x, y):
        self.length += 1

        if self.first == '':
            self.last = self.first = Node(x, '')
        else:
            self.last.next = self.last = Node(x, self.get_item(y))
    #end def

    # получение элемента списка по номеру с начала/с конца
    def get_item(self, index = '', is_back = '', is_value = '', i = 1):
        if self.first != '':
            if index != '':
                index   = (self.length - index + 1) if is_back != '' else index
                current = self.first

                if i == index:
                    return current.value if is_value != '' else current

                while current.next != '':
                    i += 1
                    current = current.next

                    if i == index:
                        return current.value if is_value != '' else current

        return ' -- no such item'
    #end def

    # удавление элемента списка по номеру
    def detele_item(self, index = '', i = 1):
        if self.first != '':
            if index != '' and index <= self.length:
                current = self.first

                if i == index:
                    self.first = self.first.next
                    return

                while current.next != '':
                    i += 1

                    if i == index:
                        current.next = current.next.next
                    else:
                        current = current.next

        return ' -- shit happens'
    #end def

    # распечатка содержимого списка
    def __str__(self):
        if self.first != '':
            current = self.first
            start = '\n\t[]'
            end   = ''
            out   = '\n\t[' + str(current.value) + '][' + str(current.next.value) + ']\n'
            i     = 1;

            while current.next != '':
                current = current.next
                postfix = '[' + str(current.next.value) + ']\n' if current.next != '' else '[]\n'
                out +=  '\t[' + str(current.value) + ']' + postfix

                if current == self.last:
                    i += 1

                    if i == 2:
                        end = ''
                        break
                    else:
                        end = '\t[]'

            return start + out + end

        return 'LinkedList []'
    #end def

    def rabbit_turtle(self, need_item = ''):
        if self.first != '':
            rabbit = self.first
            turtle = self.first
            i = 0

            while rabbit != '':
                i += 1

                print '\t' + str(rabbit.value) + '-' + str(turtle.value)

                if i > 1 and rabbit == turtle:
                    return ' -- meeting element: ' + str(rabbit.value) \
                        + '\n -- total steps: ' + str(i) \
                        + '\n -- list length: ' + str(self.length)

                rabbit = rabbit.next.next
                turtle = turtle.next

            return ' -- rabbits steps: ' + str(i) \
                + '\n -- list length: ' + str(self.length)
    #end def

    def get_cycle_start(self, start = 0):
        if self.first != '':
            rabbit = self.first
            turtle = self.first
            i = 0
            j = 0

            while rabbit != '':
                i += 1

                k = start if i == start else 1
                j = j + 1 if i > start else 0

                if i > k and rabbit == turtle:
                    if start == 0:
                        return self.get_cycle_start(i)
                    else:
                        return self.get_item(self.length - j + 1, '', 1)

                rabbit = rabbit.next.next
                turtle = turtle.next

        return ' -- rabbits steps: ' + str(i) \
            + '\n -- list length: ' + str(self.length)
    #end def
#end class

L = LinkedList()

for i in range(1, 25):
    L.add_item(i)

L.add_item_circle(100, 21)
#L.detele_item(2)
print L
#print L.get_item(23, '', 1)
print L.rabbit_turtle()
#print L.get_cycle_start()

