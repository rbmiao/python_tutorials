#!/usr/bin/python

class Node:
    def __init__(self, data):
        self.left  = None
        self.right = None
        self.data  = data
    
    def insert(self, insert_data):
        insertNode = Node(insert_data)
        ##print(insertNode.left)
        ##print(insertNode.right)
        ##print(insertNode.data)
        if insert_data < self.data:
            if self.left == None:
                self.left = insertNode
            else:
                self.left.insert(insert_data)
        elif insert_data > self.data:
            ## insert_data > self.data
            if self.right == None:
                self.right = insertNode
            else: 
                self.right.insert(insert_data)
        else:  
            self.data = insert_data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.printTree()
