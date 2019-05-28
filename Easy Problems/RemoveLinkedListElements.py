#203. Remove Linked List Elements
#Problem Link: https://leetcode.com/problems/remove-linked-list-elements/
#Remove all elements from a linked list of integers that have value val.

#Example:

#Input:  1->2->6->3->4->5->6, val = 6
#Output: 1->2->3->4->5

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyhead = ListNode(-1)
        dummyhead.next = head
        current_node=dummyhead
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return dummyhead.next

#Runtime: 56 ms, faster than 96.16% of Python online submissions for Remove Linked List Elements.
#Memory Usage: 18.8 MB, less than 18.13% of Python online submissions for Remove Linked List Elements.
