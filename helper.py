# Implementation of a Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def get_head(self): # O(1)
        return self.head
    
    def insert_at_tail(self,data): # O(n)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        curr_node.next = new_node
        return

    def is_empty(self): # O(1)
        if self.head is None:
            return True
        else:
            return False
        
    def insert_at_head(self, data): # O(1)
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node
        return self.head

    def print_list(self): # O(n)

        if self.is_empty():
            print("List is empty")
            return False
        curr_node = self.head
        while curr_node.next is not None:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print(curr_node.data, "-> None")
        return
    
    def search(self, value): # O(n)
        if self.is_empty():
            print("List is empty")
            return False
        curr_node = self.head
        while curr_node:
            if curr_node.data == value:
                return True
            curr_node = curr_node.next
        return False
    
    def recursive_search_helper(self, node, value): # O(n)
            if node is None:
                return False
            if node.data == value:
                return True
            return self.recursive_search_helper(node.next, value)
    def recursive_search(self, value):
        return self.recursive_search_helper(self.head, value)
    
    def delete_at_head(self): # O(1)
        if self.is_empty():
            return False
        temp_node = self.head # save the head node
        self.head = self.head.next # make the second node the new head node
        temp_node.next = None # set the temp node next to None
        return 
    
    def delete(self, value): # O(n)
        if self.is_empty():
            return False
        curr_node = self.head
        prev_node = None # we need to keep track of the previous node
        while curr_node:
            if curr_node.data == value:
                if prev_node:
                    prev_node.next = curr_node.next # remove the node by skipping it
                else:
                    self.delete_at_head()
                return True
            prev_node = curr_node
            curr_node = curr_node.next
        return False
    
    def delete_at_tail(self): # O(n)
        if self.is_empty():
            return False
        curr_node = self.head
        prev_node = None
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = None
        return True
    
    def reverse_iterative(self): # O(n)
        """ Reverse a linked list iteratively
        Description:
            1. Initialize three pointers prev as NULL, curr as head and next as NULL.
            2. Iterate trough the linked list. In loop, do following.
            3. Before changing next of current,
                1. store next node
                2. Now change next of current
                3. This is where actual reversing happens
            4. Move prev and curr one step forward

        """
        if self.is_empty():
            return False
        prev_node = None
        curr_node = self.head
        next_node = None
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        return True
    
    def reverse_recursive(self): # O(n)
        """ Reverse a linked list recursively
        Description:
            1. Divide the list in two parts - first node and rest of the linked list.
            2. Call reverse for the rest of the linked list.
            3. Link rest to first.
            4. Fix head pointer
        """
        def _reverse_recursive(curr_node, prev_node):
            if not curr_node:
                return prev_node
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            return _reverse_recursive(curr_node, prev_node)
        self.head = _reverse_recursive(curr_node=self.head, prev_node=None)
        return True
    
    def remove_duplicates(self): # O(n)
        if self.is_empty():
            return False
        curr_node = self.head
        prev_node = None
        seen_values = dict()
        while curr_node:
            if curr_node.data in seen_values:
                prev_node.next = curr_node.next
            else:
                seen_values[curr_node.data] = 1 
                prev_node = curr_node
            curr_node = curr_node.next
        return True

    def length_iterative(self):
        if self.is_empty():
            return 0
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count
    
    def length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)
    
    def detect_loops(self):
        if self.is_empty():
            return False
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False

def union(list1, list2):
    if list1.is_empty():
        return list2
    if list2.is_empty():
        return list1
    curr_node = list1.head
    while curr_node.next:
        curr_node = curr_node.next
    curr_node.next = list2.head
    list1.remove_duplicates()
    return list1

def intersection(list1, list2):
    if list1.is_empty() or list2.is_empty():
        return False
    seen_values = dict()
    intersecting_list = LinkedList()
    curr_node = list1.head
    while curr_node:
        seen_values[curr_node.data] = 1
        curr_node = curr_node.next
    curr_node = list2.head
    while curr_node:
        if curr_node.data in seen_values:
            intersecting_list.insert_at_head(curr_node.data)
        curr_node = curr_node.next
    return intersecting_list

def checkIfIsPalindrome(self):
    if self.is_empty():
        return False
    curr_node = self.head
    stack = []
    while curr_node:
        stack.append(curr_node.data)
        curr_node = curr_node.next
    curr_node = self.head
    while curr_node:
        data = stack.pop()
        if curr_node.data != data:
            return False
        curr_node = curr_node.next
    return True

    