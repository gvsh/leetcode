

import random
from random import choice
from typing import List, Optional

# from pydantic import BaseModel


class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

def convert_list_to_linked_list(input_list):

    dummy = ListNode(0, None)
    head = None

    if len(input_list) == 0:

        return None
    elif len(input_list) == 1:

        return ListNode(input_list[0], None)
    else:

        head = ListNode(input_list[0], None)
        dummy.next = head

        previous_node = head

        for x in input_list[1:]:
            current_node = ListNode(x, None)
            previous_node.next = current_node
            previous_node = previous_node.next

        i = 0
        current_node = dummy.next

        while current_node:

            print()
            print(f"current index: {i}")
            print(f"current node: {current_node.val}")
            print("***************")
            i = i + 1
            current_node = current_node.next

    return dummy.next

def print_list(l1):

    i = 0
    
    while l1:
        print(f"Node {i + 1} has value: {l1.val}")
        i += 1
        l1 = l1.next

        

list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [1,3,4]

l1 = convert_list_to_linked_list(list1)
# l2 = convert_list_to_linked_list(list2)

print_list(l1)
# print_list(l2)


