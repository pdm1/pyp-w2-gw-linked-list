from .interface import AbstractLinkedList
from .node import *

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=None):
        self.start = None
        self.end = None
        
        if elements:
            for elem in elements:
                self.append(elem)

    def __str__(self):
        return str([s for s in self])

    def __len__(self):
        counter = 0
        for elem in self:
            counter += 1
        return counter

    def __iter__(self):
        # set the index and loop through each elem, reassigning each time
        index = self.start
        while index:
            yield index.elem
            index = index.next
        raise StopIteration

    def __getitem__(self, index):
        for i, element in enumerate(self):
            if i == index:
                return element
        raise IndexError

    def __add__(self, other):
        my_list = LinkedList()
        
        for index in self:
            my_list.append(index)
        for index in other:
            my_list.append(index)
        return my_list

    def __iadd__(self, other):
        for index in other:
            self.append(index)
        return self

    def __eq__(self, other):
        
        if len(self) != len(other):
            return False
        
        # at index index compare both values in each list
        for index,(s,o) in enumerate(zip(self,other)):
            if s != o:
                return False
        return True
        
    def __ne__(self,other):
        return not self == other
        

    def append(self, elem):
        node = Node(elem)
    
        if self.start is None:
            self.start = node
            self.end = node
        else:
            self.end.next = node
            self.end = node

    def count(self):
        #counts each elem
        counter = 0
        for elem in self:
            counter += 1
        return counter

    def pop(self, index=None):
        if len(self) == 0:
            raise IndexError
        
        if index is None:
            index = self.count() - 1
        
        if index == 0:
            elem = self.start.elem
            self.start = self.start.next
            return elem
        
        if index >= len(self):
            raise IndexError
        
        i = 0
        
        last_node = None
        current_node = self.start
        
        while True:
            if i == index:
                last_node.next = current_node.next
                return current_node.elem
            
            last_node = current_node
            current_node = current_node.next
            
            i += 1