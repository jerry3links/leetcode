"""
    from LinkedList.solM024SwapNodes import Solution
    head = Solution().testCase()
    print("List:")
    Solution().printList(head)
    ans = Solution().swapPairs(None)
    print("ans: ")
    Solution().printList(ans)
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while p and p.next:
            # initialize
            q = p.next
            r = q.next
            # swap
            prev.next = q
            q.next = p
            p.next = r
            # take steps forward
            prev = p
            p = r

        return dummy.next

    def testCase(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(4)
        return head

    def printList(self, head):
        from customDataType import ListNode
        ListNode.printList(head)
