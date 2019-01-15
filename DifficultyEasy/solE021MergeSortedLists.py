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
        node1 = l1
        node2 = l2

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = None
        if node1.val < node2.val:
            head = ListNode(node1.val)
            node1 = node1.next
        else:
            head = ListNode(node2.val)
            node2 = node2.next

        track = head
        while node1 is not None and node2 is not None:
            if node1.val < node2.val:
                track.next = ListNode(node1.val)
                node1 = node1.next
            else:
                track.next = ListNode(node2.val)
                node2 = node2.next
            track = track.next

        if node1 is not None:
            track.next = ListNode(node1.val)
        elif node2 is not None:
            track.next = ListNode(node2.val)

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