# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
    from customDataType import ListNode
    Q = [3, 2, 0, -4]
    pos = 1

    print("Q: {}".format(Q))
    node_end = None
    val_beg = -4

    node_prv = None
    for i in range(len(Q)):
        num = Q[i]
        node = ListNode(num)
        if i == 0:
            head = node
        if i == pos:
            node_end = node
        if num == val_beg:
            node.next = node_end
        if node_prv:
            node_prv.next = node
        node_prv = node

    from DifficultyMedium.sol142LinkedListII import Solution
    ansNode = Solution().detectCycle(head)
    print("ansNode.val: {}".format(ansNode.val))
"""


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        # s = str(head.val) + " -> " + str(head.next.val) +\
        #     " -> " + str(head.next.next.val) + " -> " + str(head.next.next.next.val)

        node = head
        # nodeMap = set()
        # nodeMap.add(node)

        nodeMap = {}
        nodeMap[node] = True
        isCyclic = False

        cycleNode = None

        while node.next and not isCyclic:
            # print("curr: {}, next: {}".format(node.val, node.next.val))
            if node.next in nodeMap:
                isCyclic = True
                cycleNode = node.next
            else:
                # nodeMap.add(node.next)
                nodeMap[node.next] = True
            node = node.next

        return cycleNode
