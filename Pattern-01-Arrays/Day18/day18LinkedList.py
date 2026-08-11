'''
Hum Singly Linked List se start karenge:

Node kya hota hai
data + next
Traversal
Insert at beginning
Insert at end
Insert at position
Delete
Search
Reverse Linked List
LeetCode questions
'''
'''
Linked List Roadmap

Pattern 1 — Basics

Node
data, next
Traversal
Length
Search

Pattern 2 — Insertion

Insert at beginning
Insert at end
Insert at position

Pattern 3 — Deletion

Delete beginning
Delete end
Delete by position/value

Pattern 4 — Two Pointers

Slow & Fast pointer
Middle of Linked List
Cycle Detection

Pattern 5 — Reversal

Reverse Linked List
Reverse in groups

Pattern 6 — Merge

Merge Two Sorted Lists
Merge multiple lists

Pattern 7 — Advanced

Remove Nth Node
Reorder List
Odd Even Linked List
Palindrome Linked List
'''


class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def printSLL(self):
        t1=self.head
        while t1.next != None :
            print(t1.data)
            t1=t1.next
        print(t1.data)

    def inserAtbeg(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
    def insertAtend(self,data):
        temp=Node(data)
        if self.head != None:
            t1=self.head
            while t1.next!=None:
                t1=t1.next
            t1.next=temp

        else:
            self.head=temp

    def insertatAnyPosition(self, data, location):
        temp = Node(data)

        if self.head == None:
            return

        t1 = self.head

        while t1 != None:
            if t1.data == location:
                temp.next = t1.next
                t1.next = temp
                return

            t1 = t1.next
            '''
    def deleteAtbeg(self):
        if self.head is None:
            return

        self.head=self.head.next
    def deleteAtend(self):
        t1=self.head
        if self.head is None:
            
            return 
        if self.head.next is None:
            self.head = None
            return 
        while t1.next.next !=None:
            t1=t1.next

        t1.next=None
        '''
    def deletebyval(self,value):
        if self.head is None:
            return

    # Head delete
        if self.head.data == value:
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr:
            if curr.data == value:
                prev.next = curr.next
                return

            prev = curr
            curr = curr.next
            








obj=SinglyLinkedList()
obj.inserAtbeg(50)
obj.inserAtbeg(40)
obj.inserAtbeg(30)
obj.inserAtbeg(20)
obj.inserAtbeg(10)
obj.insertAtend(80)
obj.insertAtend(90)
obj.insertAtend(100)
obj.insertAtend(110)
obj.insertatAnyPosition(60,50)
obj.insertatAnyPosition(70,60)

'''
obj.deletebyval(10)
obj.deletebyval(50)
obj.deletebyval(110)
'''
'''
obj.deleteAtbeg()#delete10
obj.deleteAtbeg()#delete20
obj.deleteAtend()#delete110
obj.deleteAtend()#delete100
'''

obj.printSLL()