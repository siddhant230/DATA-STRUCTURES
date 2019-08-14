#node creator
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#linked list creator
class LinkedList:
    def __init__(self):
        self.head=None

    def addNode(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            currentNode=self.head
            while True:
                if currentNode.next is None:
                    break
                currentNode=currentNode.next
            currentNode.next=newNode

    def printNode(self):
        currentNode=self.head
        if currentNode is None:
            print('List is Empty')
        else:
            while True:
                if currentNode is None:
                    break
                print(currentNode.data,'=>',end='')
                currentNode=currentNode.next

    def searchNode(self,name):
        found=0
        currentNode=self.head
        while True:
            if currentNode.data==name:
                found=1
                break
            if currentNode.next is None:
                break
            currentNode=currentNode.next
        if found==1:
            print('Found')
        else:
            print('Not Found')

    def deleNode(self,name):
        currentNode=self.head
        previousNode=None
        if currentNode.data==name:
            self.head=currentNode.next
        else:
            while True:
                if currentNode.data==name:
                    previousNode.next=currentNode.next
                    break
                if currentNode.next is None:
                    break
                previousNode=currentNode
                currentNode=currentNode.next
##coder definition zone
'''node1=node('a')
node2=node('b')
node3=node('c')
node4=node('d')
node5=node('e')
list=LinkedList()
list.addNode(node1)
list.addNode(node2)
list.addNode(node3)
list.addNode(node4)
list.addNode(node5)
list.deleNode('e')
list.searchNode('a')
list.printNode()'''

node_holder=[]
list=LinkedList()

def noder():
    n=int(input('how many nodes you want to insert? : '))
    for i in range(n):
        node_holder.append(node(input('Enter the data/name here for Node '+str(i)+' : ')))
        list.addNode(node_holder[-1])
while True:
    if len(node_holder)<3:
        print('List almost Empty fill some Values first')
        print('Press y to fill value otherwise press anyother key')
        response=input('response : ')
        if response=='y' or response=='Y':
            noder()
        elif response=='n' or response=='N' and len(node_holder)==0:
            print("can't be operated further")
            quit()

    print('Enter 1 for search\nEnter 2 for deletion\nEnter 3 for printing you List')
    ch=int(input('Your choice : '))
    if ch==1:
        name=input('Enter the name you want to Search : ')
        list.searchNode(name)
        while True:
            print('press any key to continue , press q to quit')
            response=input('response : ')
            if response=='q':
                break
            else:
                name=input('Enter the name you want to Search : ')
                list.searchNode(name)
    if ch==2:
        name=input('Enter the name you want to Delete : ')
        list.deleNode(name)
        while True:
            print('press any key to continue , press q to quit')
            response=input('response : ')
            if response=='q':
                break
            else:
                name=input('Enter the name you want to Delete : ')
                list.deleNode(name)
    if ch==3:
        list.printNode()
        print()
    print('press any key to continue , press q to quit')
    response=input('response : ')
    if response=='q':
        break
