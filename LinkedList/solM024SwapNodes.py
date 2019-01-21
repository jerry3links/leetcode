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
        if head is None:
            return head

        cnt = 0

        track = head
        new_head = track
        while track:
            previous = track
            track = track.next
            if track:
                print("{} and {}".format(previous.val, track.val))
            else:
                print("{} and {}".format(previous.val, None))
            cnt += 1

        return new_head.next





    def testCase(self):
        head = ListNode(1)
        head.next = ListNode(2)
        # head.next.next = ListNode(3)
        # head.next.next.next = ListNode(4)
        return head

    def printList(self, head):
        from customDataType import ListNode
        ListNode.printList(head)
