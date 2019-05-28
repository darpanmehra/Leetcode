#21. Merge Two Sorted Lists
#Problem Link: "https://leetcode.com/problems/merge-two-sorted-lists/"
#Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

#Example:
#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next,l1)
            return l2

#Runtime: 44 ms, faster than 86.58% of Python3 online submissions for Merge Two Sorted Lists.
#Memory Usage: 13.2 MB, less than 37.47% of Python3 online submissions for Merge Two Sorted Lists
