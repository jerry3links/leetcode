# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printTree(root):

        depth = TreeNode.checkDepth(root, 0)
        cnt = 0
        toCheck = [root]
        node_list = []
        while toCheck:
            tmp = []
            for x in toCheck:
                node_list.append(x)
                if x:
                    tmp.append(x.left)
                    tmp.append(x.right)
            cnt += 1
            toCheck = tmp

        cnt = 0
        for i in range(depth):
            line = ""
            for j in range(2**i):
                val = str(node_list[cnt].val) if node_list[cnt] else 'N'
                cnt += 1
                line += "".join([" " for _ in range((2 ** (depth - i)) - 1)])
                line += val

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
