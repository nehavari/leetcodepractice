# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = 1
        right = head
        
        while right.next:
            length += 1
            right = right.next
            
        if k > length:
            k = k % length
        elif k == length:
            return head
        
        left = head
        
        for _ in range(length - k - 1):
            left = left.next
        
        right.next = head   
        head = left.next
        left.next = None
        
        return head
        