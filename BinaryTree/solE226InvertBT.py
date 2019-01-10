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
    Solution.printTree(root)
    new_root = Solution().invertTree(root)
    print("Inverted tree:")
    Solution.printTree(new_root)
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

    @staticmethod
    def printTree(root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
