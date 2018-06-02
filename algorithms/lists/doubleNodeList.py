#!/usr/bin/env python
# -*- coding: utf-8 -*-

#класс Node для определения элемента списка
class Node:
    def __init__(self, value = '', prev = '', next = ''):
        self.value = value
        self.prev  = prev
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
    def addItem(self, x):
        self.length += 1

        if self.first == '':
            self.last = self.first = Node(x, '', '')
        else:
            self.last.next = self.last = Node(x, self.last.value, '')
    #end def

    # добавление кольцевого элемента списка
    def addItemCircle(self, x, y):
        self.length += 1

        if self.first == '':
            self.last = self.first = Node(x, '')
        else:
            self.last.next = self.last = Node(x, self.last.value, self.getItem(y))
    #end def

    # получение элемента списка по номеру
    def getItem(self, index = '', i = 1):
        if self.first != '':
            if index != '':
                current = self.first

                if i == index:
                    return current

                while current.next != '':
                    i += 1
                    current = current.next

                    if i == index:
                        return current

        return ' --no such item'
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
                        current.next.prev = current.value
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
            out   = '\n\t[][' + str(current.value) + '][' + str(current.next.value) + ']\n'
            i     = 1;

            while current.next != '':
                current = current.next
                postfix = '[' + str(current.next.value) + ']\n' if current.next != '' else '[]\n'
                out +=  '\t[' + str(current.prev) + '][' + str(current.value) + ']' + postfix

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

#end class

L = LinkedList()

for i in range(1, 20):
    L.addItem(i)

#L.addItemCircle(100, 14)

L.detele_item(17)
print L