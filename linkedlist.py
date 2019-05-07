#!/usr/bin/python

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
        #self.nextval = None

    def printlinkedlist(self):
        printp = self.headval
        while printp is not None:
            print(printp.dataval)
            printp = printp.nextval

    def atBeginning(self, newData):
        beginNode = Node(newData)
        beginNode.nextval = self.headval
        self.headval = beginNode  
        
    def insertAtBack(self, backdata):
        backNode = Node(backdata)
        if self.headval == None:
            self.headval = backNode
            return
        lastp = self.headval
        while lastp.nextval:
            lastp = lastp.nextval    
        lastp.nextval = backNode
    def insertbetween(self, middlenode, insertdata):
        if middlenode == None:
            print("The mentioned node is absent!")
            return

        insertNode = Node(insertdata)
        ## insertNode.dataval
        ## insertNode.nextval        
        insertNode.nextval = middlenode.nextval
        middlenode.nextval = insertNode




list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
list1.headval.nextval =e2
e3 = Node("Wed")
e2.nextval = e3
e4 = Node("Thursday")
e3.nextval = e4
list1.printlinkedlist()


list1.atBeginning("Sunday")
list1.printlinkedlist()

list1.insertAtBack("Friday")
list1.printlinkedlist()


print("#########Rongbing")
list1.insertbetween(e2, 'midTueWed')
list1.printlinkedlist()