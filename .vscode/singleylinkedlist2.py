#insert at tne front of linkedlist
class Node:
    def __init__(self,d):
        self.data=d
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeg(self,x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode
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
    l.insertatbeg(x)
l.printlist() 
































