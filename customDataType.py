# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def printList(head):
        node = head
        line = ""
        while node:
            line += str(node.val) + " -> "
            node = node.next
        print(line)

class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printTree(root):

        if root is None:
            return

        depth = TreeNode.checkDepth(root, 0)
        node_list = [-1 for _ in range(2**depth-1)]
        toCheck = [(root, 0)]
        while toCheck:
            node, parent_idx = toCheck.pop(0)
            if node:
                node_list[parent_idx] = node.val
                toCheck.append((node.left, 2 * parent_idx + 1))
                toCheck.append((node.right, 2 * parent_idx + 2))

        # cnt = 0
        for i in range(depth):
            line = ""
            for j in range(2**i):
                idx = 2**i + j - 1
                val = 'N' if node_list[idx] == -1 else str(node_list[idx])
                line += "".join([" " for _ in range((2 ** (depth - i)) - 1)])
                line += val #"{:02d}".format(idx)

            print(line)

    @staticmethod
    def checkDepth(node, level_from):

        if node is None:
            return level_from

        return max(TreeNode.checkDepth(node.left, level_from+1),
                   TreeNode.checkDepth(node.right, level_from+1))


class Queue:
    def __init__(self, x):
        self.maxS = x
        self.list = []
        self.size = 0

    def enQ(self, x):

        if self.size >= self.maxS:
            return False

        self.list.append(x)
        return True
