#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

# класс BinaryNode для определения элемента дерева
class BinaryNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    #end def
#end class

# класс, описывающий само дерево
class BinaryTree:
    def createNode(self, data):
        return BinaryNode(data)
    # end def

    def insert(self, node, data):
        if node == None:
            return self.createNode(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        elif data > node.data:
            node.right = self.insert(node.right, data)

        return node
    # end def

    def treePrint(self, root, side=None, level=0):
        if root != None:
            sufix = side * level if (side != None and level > 0) else ''
            level += 1

            self.treePrint(root.left, '-l', level)
            print('\t' + str(root.data) + sufix)
            self.treePrint(root.right, '-r', level)
    # end def

    def treeHeight(self, node, width=None):
        if node == None:
            return 0
        else:
            lheight = self.treeHeight(node.left)
            rheight = self.treeHeight(node.right)

            if width != None:
                return lheight + 1 + rheight
            else:
                if lheight > rheight:
                    return lheight + 1
                else:
                    return rheight + 1
    # end def

    def treeElementData(self, root, type):
        if root == None:
            return None
        else:
            if type == 'max':
                element_data = self.treeElementData(root.right, type)
                return element_data if element_data and element_data > root.data else root.data
            else:
                element_data = self.treeElementData(root.left, type)
                return element_data if element_data and element_data < root.data else root.data
    # end def

    def treeElementsCount(self, root):
        if root == None:
            return 0

    # end def

# end class


def main():
    BTree = BinaryTree()
    root = BTree.insert(None, 30)

    BTree.insert(root, 20)
    BTree.insert(root, 10)
    BTree.insert(root, 25)
    BTree.insert(root, 60)
    BTree.insert(root, 54)
    BTree.insert(root, 70)
    BTree.insert(root, 53)
    BTree.insert(root, 55)
    BTree.insert(root, 80)
    BTree.insert(root, 90)

    print('\n')
    BTree.treePrint(root)
    print('\n-- Height is: ' + str(BTree.treeHeight(root)))
    print('\n-- Widht is: ' + str(BTree.treeHeight(root, 1)))
    print('\n-- Min element is: ' + str(BTree.treeElementData(root, 'min')))
    print('\n-- Max element is: ' + str(BTree.treeElementData(root, 'max')))

# end def

if __name__ == "__main__":
    main()
