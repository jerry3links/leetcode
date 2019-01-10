# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    from BinaryTree.solM129SumRootToLeaf import Solution
    root = Solution().constructCase()
    Solution().printTree(root)
    ans = Solution().sumNumbers(None)
    print(ans)
"""


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        queue = [root]
        ans = 0
        while queue:
            node = queue.pop(0)
            if node.left == node.right is None:
                ans += node.val
            if node.left:
                node.left.val += node.val * 10
                queue.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                queue.append(node.right)


        return ans

    def constructCase(self):
        from customDataType import TreeNode
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        root.left.left.left = TreeNode(8)
        return root

    def constructCase2(self):
        from customDataType import TreeNode
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        # root.left.right = TreeNode(3)
        # root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        return root

    @staticmethod
    def printTree(root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
