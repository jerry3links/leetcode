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
        tree = self.bfs(root)
        print(tree)
        targets = [i for i in range(len(tree)) if tree[i] is not None]
        print(targets)

        # for idx in targets:
        a = self.pathSum(2, tree, targets)
        print(a)


    def pathSum(self, i, tree, targets):
        toCheck = [(i, tree[i])]
        while toCheck:
            t, v = toCheck.pop(0)
            p = (t - 2) / 2 if t % 2 == 0 else (t - 1) / 2
            if p in targets:
                toCheck.append((p, tree[p]))
            l = 2 * t + 1
            if l in targets:
                toCheck.append((l, tree[l]))
            r = 2 * t + 2
            if r in targets:
                toCheck.append((r, tree[r]))



            # node_list[parent_idx] = node.val
            # toCheck.append(t)
            # toCheck.append(t)


    def bfs(self, root):
        depth = self.maxDepth(root, 0)
        node_list = [None for _ in range(2**depth-1)]
        toCheck = [(root, 0)]
        while toCheck:
            node, parent_idx = toCheck.pop(0)
            if node:
                node_list[parent_idx] = node.val
                toCheck.append((node.left, 2 * parent_idx + 1))
                toCheck.append((node.right, 2 * parent_idx + 2))
        return node_list

    def maxDepth(self, root, cnt = 0):
        if root is None:
            return cnt
        return max(self.maxDepth(root.left, cnt),
                   self.maxDepth(root.right, cnt)) + 1

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

        root.right = TreeNode(3)
        root.right.left = TreeNode(-1)
        root.right.right = TreeNode(4)
        return root


    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
