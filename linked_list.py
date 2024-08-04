class Node:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=None
    
class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self,value):
        if self.head is None:
            self.head=Node(value)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=Node(value)
    def prepend(self,value):
        if self.head is None:
            self.head=Node(value)
        curr=Node(value)
        curr.next=self.head
        self.head=curr
        


    def display(self):
        curr=self.head
        while curr:
            print(f"{curr.val}",end=" -> ")
            curr=curr.next
        print("None")

l=LinkedList()
l.append(7)
l.append(8)
l.append(9)
l.append(10)
l.prepend(6)
l.display()