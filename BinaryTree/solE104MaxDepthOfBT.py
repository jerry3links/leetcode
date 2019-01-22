"""
    from BinaryTree.solE104MaxDepthOfBT import Solution
    root = Solution().testCase()
    print("Tree:")
    Solution().printTree(root)
    ans = Solution().maxDepth(root)
    print("ans: {}".format(ans))
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root, depth = 0):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return depth

        return max(self.maxDepth(root.left, depth + 1),
                   self.maxDepth(root.right, depth + 1))


    def testCase(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root

    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
