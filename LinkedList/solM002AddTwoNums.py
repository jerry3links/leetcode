"""
    from LinkedList.solM002AddTwoNums import Solution
    l1, l2 = Solution().testCase()
    print("l1:")
    Solution().printList(l1)
    print("l2:")
    Solution().printList(l2)
    ans = Solution().addTwoNumbers(l1,l2)
    print("ans:")
    Solution().printList(ans)
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        track = ListNode(0)
        head = track
        overflow = 0
        while l1 or l2:
            s = 0
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next

            s += overflow
            track.val = s % 10
            overflow = int(s / 10)
            # print("s: {}, val: {}, ov: {}".format(s, track.val, overflow))
            if l1 or l2:
                track.next = ListNode(0)
                track = track.next

        if l1 is None and l2 is None:
            if overflow > 0:
                track.next = ListNode(overflow)

        return head


    def testCase(self):
        head1 = ListNode(1)
        # head1.next = ListNode(4)
        # head1.next.next = ListNode(3)

        head2 = ListNode(9)
        head2.next = ListNode(9)
        # head2.next.next = ListNode(4)

        return head1, head2

    def printList(self, head):
        from customDataType import ListNode
        ListNode.printList(head)