# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = []
        new.append(head[-1])
        i = 2
        while i <= len(head):
            item = head[-i]
            new.append(item)
            i += 1 

        return new