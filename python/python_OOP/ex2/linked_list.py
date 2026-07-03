#This module is the implementation of a linked list, and a single node
#Author: Gal ELhiani
#Tester: Meytar

class Node:
    """a class representing a single node in a linked list."""
    def __init__(self, val, next):
        '''initializes a Node'''
        self.val = val
        self.next = next
    
    def __str__(self):
        '''a function to print the node'''
        return str(self.val)


class LinkedList:
    """a class representing a singly linked list with O(1) length tracking."""
    def __init__(self, head=None, tail=None):
        """initializes a LinkedList, calculates the starting length."""
        self.count = 0
        self.head = head
        self.tail = tail
        
        #while loop to calculate initial size of list
        current = self.head
        while current is not None:
            current = current.next
            self.count += 1

    def is_empty(self):
        """a function that checks if the linked list is empty."""
        if self.head == None:
            return True
        return False

    def push(self, value):
        """a function that appends a new node containing 'value' to the back of the list."""
        new_node = Node(value, None)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1 

    def pop(self):
        """a function that removes and returns the node at the front of the list."""
        if self.is_empty():
            return None

        temp = self.head
        self.head = self.head.next
        
        if self.head == None:
            self.tail = None
            
        self.count -= 1 
        return temp
    
    def get_head(self):
        """a function that returns the front node of the list."""
        if self.is_empty():
            return None
        return self.head
    
    def get_len(self):
        """a function thatreturns the current number of nodes in the list"""
        return self.count
    
    def __str__(self):
        if self.is_empty():
            return "Empty"
        
        current = self.head
        output = ""
        while current is not None:
            output+= f"{current.val} -> "
            current = current.next
        output += "None"
        return output