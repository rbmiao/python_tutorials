#!/usr/bin/python
        
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SLinkedList:
    def __init__(self):
        self.head = None
        
    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode
        		
    # Function to remove node
    def RemoveNode(self, Removekey):
        
        HeadVal = self.head
        
        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        
        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        
        if (HeadVal == None):
            return
        
        prev.next = HeadVal.next
        
        HeadVal = None
        
    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next
        

llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue1")
llist.Atbegining("Tue2")
llist.Atbegining("Tue3")
llist.Atbegining("Tue4")
llist.Atbegining("Wed1")
llist.Atbegining("Wed2")
llist.Atbegining("Wed3")
llist.Atbegining("Thu1")
llist.Atbegining("Thu2")
llist.Atbegining("Thu3")
llist.LListprint()
print("Start to remove...._Tue_..")
llist.RemoveNode("Thu2")
llist.LListprint()