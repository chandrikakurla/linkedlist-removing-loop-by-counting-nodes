#creating nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #creating newnodes and inserting into linkedlist
    def insert(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastnode=self.head
        while(lastnode.next is not None):
            lastnode=lastnode.next
        lastnode.next=newnode
    #printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        while(currentnode is not None):
            print(currentnode.data)
            currentnode=currentnode.next
    #detecting loop in linkedlist
    def detect_loop(self):
        slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("loop is present")
                self.removeloop(slow)
                return
        print("loop is not present")
        return
    #removing loop in linkedlist
    def removeloop(self,refnode):
        #counting no.of nodes in loop
        k=1
        pointer1=pointer2=refnode
        while(pointer1.next is not pointer2):
            pointer1=pointer1.next
            k=k+1
        pointer1=self.head
        pointer2=self.head
        #pointing pointer2 to k steps next to headnode
        for i in range(k):
            pointer2=pointer2.next
        #making pointer1 and pointer2 pointing to the starting of the loop
        while(pointer1!=pointer2):
            pointer1=pointer1.next
            pointer2=pointer2.next
        #making pointer2 to point end of loop/linkedlist
        while(pointer2.next!=pointer1):
            pointer2=pointer2.next
        pointer2.next=None
        
if __name__=="__main__":
    llist=LinkedList()
    llist=LinkedList()
    for i in range(1,7):
        llist.insert(i)
    #creatingloop in linkedlist
    llist.head.next.next.next.next.next.next=llist.head
    llist.detect_loop()
    llist.printllist()


                

