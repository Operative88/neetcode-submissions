# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # zapamiętaj następnika, zaraz go stracisz
            curr.next = prev     # odwróć strzałkę
            prev = curr          # przesuń prev do przodu
            curr = nxt           # przesuń curr do przodu

        return prev