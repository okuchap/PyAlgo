#Implement Deque in Python

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        #note how to judge whether the list is empty or not
        return self.items == []

    def addFront(self, item):
        #note that we assign the O(1) acction to addFront
        self.items.append(item)

    def addRear(self, item):
        #O(n)
        self.items.append(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
