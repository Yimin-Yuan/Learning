# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return []
        p=head
        q=p.next
        p.next=None
        while q:
            r=q.next
            q.next=p
            p=q
            q=r
        return p
        
        
