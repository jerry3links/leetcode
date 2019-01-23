"""
    from BinaryTree.solE110BalancedBT import Solution
    root = Solution().testCase()
    print("Tree:")
    Solution().printTree(root)
    ans = Solution().isBalanced(root)
    print("ans: {}".format(ans))
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.depth(root) != -1:
            return True
        return False

    # bottom-up
    def depth(self, root):
        if root is None:
            return 0
        depthL = self.depth(root.left)
        depthR = self.depth(root.right)
        if depthL == -1:
            return -1
        if depthR == -1:
            return -1
        diff = depthR - depthL if depthR > depthL else depthL - depthR
        if diff > 1:
            return -1
        return max(depthR, depthL) + 1


    # O(n2)
    def topDown(self, root):
        if root is None:
            return True

        L = self.maxDepth(root.left)
        R = self.maxDepth(root.right)

        diff = L - R if L > R else R - L

        if diff <= 1 and self.topDown(root.left) and self.topDown(root.right):
            return True
        else:
            return False

    def maxDepth(self, root):
        if root is None:
            return 0

        return max(self.maxDepth(root.left),
                   self.maxDepth(root.right)) + 1

    def testCase(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        # root.left.right = TreeNode(4)
        root.left.left = TreeNode(15)
        # root.left.left.left = TreeNode(7)
        root.right = TreeNode(20)
        # root.right.left = TreeNode(15)
        # root.right.right = TreeNode(7)
        return root


    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
