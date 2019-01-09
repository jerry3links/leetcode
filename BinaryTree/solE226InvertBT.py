# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    from BinaryTree.solE226InvertBT import Solution
    root = Solution().constructCase()
    print("Original tree:")
    Solution().printTree(root)
    new_root = Solution().invertTree(root)
    print("Inverted tree:")
    Solution().printTree(new_root)
"""


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            tmp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(tmp)

        return root

    def constructCase(self):
        from customDataType import TreeNode
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        return root

    def printTree(self, root):
        depth = self.checkDepth(root, 0)
        toCheck = [root]
        node_list = []
        while toCheck:
            tmp = []
            for x in toCheck:
                if x is not None:
                    node_list.append(x.val)
                    tmp.append(x.left)
                    tmp.append(x.right)
            toCheck = tmp

        for i in range(depth):
            line = ""
            for _ in range(2**i):
                line += "".join([" " for _ in range((2 ** (depth - i)) - 1)])
                line += str(node_list.pop(0))
            print(line)

    def checkDepth(self, node, level_from):

        if node is None:
            return level_from

        return max(self.checkDepth(node.left, level_from+1),
                   self.checkDepth(node.right, level_from+1))
