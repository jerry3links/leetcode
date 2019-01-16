
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    from LinkedList.solE206ReversedLinkedList import Solution
    head = Solution().testCase()
    Solution().printList(head)
    ans = Solution().reverseList(head)
    Solution().printList(ans)
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        previous = None
        track = head

        new_head = None
        while track:
            new_head = track
            track = track.next
            new_head.next = previous
            previous = new_head

        return new_head


    def testCase(self):
        from customDataType import ListNode
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        head.next.next.next.next = ListNode(5)
        return head

    def printList(self, head):
        from customDataType import ListNode
        ListNode.printList(head)
