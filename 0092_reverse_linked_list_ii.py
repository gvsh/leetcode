# Definition for singly-linked list.

from typing import Optional


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_all(self):
        cur = self
        while cur:
            print(cur.val, end=' -> ')
            cur = cur.next
        print('None')


class Solution:
    
    def reverseBetween(
        self, head: Optional[ListNode], m: int, n: int
    ) -> Optional[ListNode]:
        
        # Empty list
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, prev = head, None

        while m > 1:
            prev = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, prev

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = prev
            prev = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
    

# 1 -> 2 -> 3 -> 4 -> 5
# 1 -> 4 -> 3 -> 2 -> 5
# 1 -> 4 -> 3 -> 2 -> 5 -> 6
# 1 -> 4 -> 3 -> 2 -> 5 -> 6 -> 7

if __name__ == '__main__':

    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l1.print_all()
    Solution().reverseBetween(l1, 2, 4).print_all()
    Solution().reverseBetween(l1, 2, 5).print_all()
    # Solution().reverseBetween(l1, 2, 6).print_all()
    # Solution().reverseBetween(l1, 2, 7).print_all()
    
    # Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 5).print_all()
    # Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 4).print_all()
    # Solution().reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 1, 3).print_all()

