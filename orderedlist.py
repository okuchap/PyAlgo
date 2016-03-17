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

#Then, construct the ordered list class, using nodes.

class OrderedList:
    def __init__(self):
        #head is a reference to the first node.
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        #implement traversal
        while current != None:
            count += 1
            current = current.getNext()

        return count

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

    def search(self,item):
        current = self.head
        found = False
        #Add another variable "stop"
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True

        return found

    def add(self,item):
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)

        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNExt(temp)







