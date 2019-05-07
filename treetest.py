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
            if self.right == None:
                self.right = insertNode
            else: 
                self.right.insert(insert_data)
        else:  
            self.data = insert_data

##print("\n\naaaaaaaaaaaa")
root = Node(9)
##print("root: left is {}".format(root.left))
##print("right is {}".format(root.right))
print("root.data is {}".format(root.data))


##print("\n\nbbbbbbbbbbbbbb")
newNode = Node(10)
##print(newNode)
##print("newNode: left is {}".format(newNode.left))
##print("right is {}".format(newNode.right))
print("newNode.data is {}".format(newNode.data))

##print("\n\ncccccccccccccc")
if newNode.data < root.data :
    if root.left == None:
        root.left = newNode
    else: 
       root.left.insert(data)     
else:
    root.right = newNode

print("left is {}".format(root.left))
print("right is {}".format(root.right))
#print("data is {}".format(root.data))
print("right.data is {}".format(root.right.data))

##print("\n\ndddddddddddddd")
##print(root.left.data)
###print(root.right.data)

##newNode.insert('15')