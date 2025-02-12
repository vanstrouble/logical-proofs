#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.
#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    linked_list = SinglyLinkedList()

    while head1:
        while head2 and head2.data <= head1.data:
            linked_list.insert_node(head2.data)
            head2 = head2.next
        
        linked_list.insert_node(head1.data)
        head1 = head1.next
    
    while head2:
        linked_list.insert_node(head2.data)
        head2 = head2.next

    return linked_list.head

# def mergeLists(head1, head2):
#     # create a dummy node for the new linked list
#     dummy = SinglyLinkedListNode(0)
#     tail = dummy
    
#     # pointers to the current nodes in both lists
#     node1, node2 = head1, head2
    
#     while node1 and node2:
#         # compare the values of the current nodes
#         if node1.data <= node2.data:
#             tail.next = node1
#             node1 = node1.next
#         else:
#             tail.next = node2
#             node2 = node2.next
#         # move the tail pointer to the last node in the new list
#         tail = tail.next
    
#     # add the remaining nodes from either list
#     if node1:
#         tail.next = node1
#     if node2:
#         tail.next = node2
    
#     # return the head of the new linked list (skipping the dummy node)
#     return dummy.head



if __name__ == '__main__':
    pass
