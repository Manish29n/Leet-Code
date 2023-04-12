# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        c=0
        temp=ListNode()
        temp=head
        while(head):
            c+=1
            head=head.next
        c=c//2
        while(c!=0):
            c-=1
            temp=temp.next
        return temp
        """
        :type head: ListNode
        :rtype: ListNode
        """
