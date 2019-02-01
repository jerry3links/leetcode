"""
    from BinaryTree.solE112PathSum import Solution
    root, sum = Solution().testCase()
    print("Tree (sum: {}): ".format(sum))
    Solution().printTree(root)
    ans = Solution().hasPathSum(root, sum)
    print("ans: {}".format(ans))
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        toCheck = [(root, sum - root.val)]

        while toCheck:
            node, remain = toCheck.pop(0)
            # print("got [{}], remain: {} ...".format(node.val, remain))
            if node.left is None and node.right is None and remain == 0:
                return True
            if node.left:
                toCheck.append((node.left, remain - node.left.val))
            if node.right:
                toCheck.append((node.right, remain - node.right.val))

        return False


    def testCase(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)

        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        return root, 22

    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
