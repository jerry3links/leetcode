"""
    from DifficultyMedium.sol109ListToBST import Solution
    from customDataType import ListNode
    Q = [-10, -3, 0, 5, 9]
    node = ListNode(Q.pop(0))
    head = node
    while Q:
        node.next = ListNode(Q.pop(0))
        node = node.next
    ans = Solution().sortedListToBST(head)

"""

from customDataType import TreeNode
from customDataType import ListNode

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        node = head
        if node is None:
            return None
        if node.next is None:
            return TreeNode(node.val)

        # transfer linked list to array
        array_whole = [node.val]
        while node.next:
            node = node.next
            array_whole.append(node.val)

        mid = int(len(array_whole) / 2)
        root = TreeNode(array_whole[mid])

        # split the array
        array_l = array_whole[:mid]
        array_r = [] if mid == len(array_whole) - 1 else array_whole[mid+1:]

        # processing left
        if len(array_l) > 0:
            node = ListNode(array_l.pop(0))
            head_l = node
            while array_l:
                node.next = ListNode(array_l.pop(0))
                node = node.next
            root.left = self.sortedListToBST(head_l)
        else:
            root.left = None

        # processing right
        if len(array_r) > 0:
            node = ListNode(array_r.pop(0))
            head_r = node
            while array_r:
                node.next = ListNode(array_r.pop(0))
                node = node.next
            root.right = self.sortedListToBST(head_r)
        else:
            root.right = None

        return root
