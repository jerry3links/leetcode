"""
    from BinaryTree.solH124BTMaxPathSum import Solution
    root = Solution().testCase()
    print("Tree:")
    Solution().printTree(root)
    ans = Solution().maxPathSum(root)
    print("ans: {}".format(ans))
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        neighbors = {}
        self.DFS(root, neighbors)
        ans = max()

    def pathSum(self, v, neighbors):
        return
        # toCheck = [v]
        # while




    def DFS(self, root, neighbors = {}):
        if root is None:
            return
        node_l = root.left
        node_r = root.right
        if node_l:
            if root.val in neighbors:
                neighbors[root.val].append(node_l.val)
            else:
                neighbors[root.val] = [node_l.val]
            neighbors[node_l.val] = [root.val]
        if node_r:
            if root.val in neighbors:
                neighbors[root.val].append(node_r.val)
            else:
                neighbors[root.val] = [node_r.val]
            neighbors[node_r.val] = [root.val]

        self.DFS(root.left, neighbors)
        self.DFS(root.right, neighbors)




    def testCase(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        return root

    def testCase2(self):
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        return root

    def testCase3(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right = TreeNode(4)
        return root

    def testCase4(self):
        root = TreeNode(-5)
        root.left = TreeNode(2)
        root.left.left = TreeNode(-1)
        root.left.right = TreeNode(4)
        root.right = TreeNode(3)
        return root


    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
