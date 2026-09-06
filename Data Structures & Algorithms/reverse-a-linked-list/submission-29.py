# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # BAZA REKURENCJI: pusta lista lub ostatni element
        if not head or not head.next:
            return head

        # Rekurencyjnie odwracamy resztę listy
        newHead = self.reverseList(head.next)

        # Obracamy wskaźnik: następnik mojego następnika ma wskazywać na mnie
        head.next.next = head
        # Odcinamy stare połączenie w przód
        head.next = None

        # Zwracamy nową głowę listy (przepychaną z samego końca)
        return newHead