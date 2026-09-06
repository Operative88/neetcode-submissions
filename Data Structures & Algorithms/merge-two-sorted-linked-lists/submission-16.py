# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        # pętla przerywa działanie, gdy przynajmniej jedna z list się wyczerpie
        while list1 and list2: 
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # wszystkie węzły wewnątrz list1 lub list2 są już połączone wskaźnikami
        # wystarczy podpiąc pierwszy z pozostałych elementów, a reszta elementów będzie dołączona
        # bez tej linijki, jeśli jedna lista byłaby dłuższa od drugiej jej końcowe wartości zostałyby pominięte w w wyniku końcowym
        tail.next = list1 or list2

        return  dummy.next
