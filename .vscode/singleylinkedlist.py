class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertend(self,x):
        newnode=Node(x)
        if self.head is None:
            self.head=newnode
            return
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=newnode
    def printlist(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.next
        print()
n=int(input("enter no of nodes:"))
l=linkedlist()
for i in range(n):
    x=int(input())
    l.insertend(x)
l.printlist() 
