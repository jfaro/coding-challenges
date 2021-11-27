# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        merged_list_head = ListNode(0)
        merged_list_tail = merged_list_head

        while list1 and list2:
            if list1.val > list2.val:
                merged_list_tail.next = list2
                list2 = list2.next
            else:
                merged_list_tail.next = list1
                list1 = list1.next

            merged_list_tail = merged_list_tail.next

        merged_list_tail.next = list1 or list2

        return merged_list_head.next
