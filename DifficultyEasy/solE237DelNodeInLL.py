# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    from customDataType import ListNode
    head = ListNode(4)
    head.next = ListNode(5)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(9)

    from DifficultyEasy.solE237DelNodeInLL import Solution
    Solution().deleteNode(head.next)
    node = head
    ans = ""
    while node != None:
        ans += str(node.val) + " "
        node = node.next
    print(ans)

"""


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        previous = None
        while node is not None:
            if node.next is None and previous is not None:
                previous.next = None
                break
            node.val = node.next.val
            previous = node
            node = node.next


    def constructCase(self, lst, target_val):
        from customDataType import ListNode

        node = ListNode(lst.pop(0))
        target_node = None
        if node.val == target_val:
            target_node = node

        head = node
        while lst:
            node.next = ListNode(lst.pop(0))
            if node.val == target_val:
                target_node = node
            node = node.next

        return head, target_node
