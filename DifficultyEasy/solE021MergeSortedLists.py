# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    from DifficultyEasy.solE021MergeSortedLists import Solution
    l1, l2 = Solution().constructCase()
    print("l1:")
    Solution().printList(l1)
    print("l2:")
    Solution().printList(l2)
    ans = Solution().mergeTwoLists(None, None)
    print("ans:")
    Solution().printList(ans)
"""

from customDataType import ListNode

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = ListNode(float("-inf"))

        track = head

        while l1 and l2:

            if l1.val < l2.val:
                track.next = l1
                l1 = l1.next
            else:
                track.next = l2
                l2 = l2.next

            track = track.next

        track.next = l1 or l2

        return head.next



    def firstImpl(self, l1, l2):

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        ptr1 = l1
        ptr2 = l2

        if ptr1.val < ptr2.val:
            head = ListNode(ptr1.val)
            ptr1 = ptr1.next
        else:
            head = ListNode(ptr2.val)
            ptr2 = ptr2.next

        track = head
        while ptr1 is not None or ptr2 is not None:

            val1 = ptr1.val if ptr1 else float("inf")
            val2 = ptr2.val if ptr2 else float("inf")

            if val1 < val2:
                track.next = ListNode(val1)
                ptr1 = ptr1.next if ptr1 else None
            else:
                track.next = ListNode(val2)
                ptr2 = ptr2.next if ptr2 else None

            track = track.next

        return head

    # 1->2->4, 1->3->4
    def constructCase(self):
        from customDataType import ListNode
        head1 = ListNode(1)
        head1.next = ListNode(2)
        head1.next.next = ListNode(4)

        head2 = ListNode(1)
        head2.next = ListNode(3)
        head2.next.next = ListNode(4)
        return head1, head2

    def printList(self, head):
        from customDataType import ListNode
        ListNode.printList(head)