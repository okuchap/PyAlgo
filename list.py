#Implement an unordered list, using the node

#First, we construct the node class.
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext
        #self.next refers to another node

#Then, we construct the unordered list class, using nodes.
#Note that a list itself doesn't contain nodes as its elements. It contains only its head.

class UnorderedList:
    def __init__(self):
        #head is a reference to the first node.
        self.head = None

    def isEmpty(self):
        return self.head == None

    #Note that the new item is to be referred by the head
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        #implement traversal
        while current != None:
            count += 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            #In case the first element corresponds to the item to be removed
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        #add the item to the end of the list cf:add is to add the item to the beginning of the list
        #item is a node
        if self.size == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            while current != None:
                previous = current
                current = current.getNext()
            previous.next = item








