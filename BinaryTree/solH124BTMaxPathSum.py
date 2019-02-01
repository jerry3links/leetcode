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
        # root wont be none
        self.val_max = root.val
        self.helper(root)
        return self.val_max

    def helper(self, root):
        if root is None:
            return 0
        val_l = max(self.helper(root.left), 0)
        val_r = max(self.helper(root.right), 0)
        self.val_max = max(self.val_max, root.val + val_l + val_r)
        return max(root.val + val_l, root.val + val_r)


    # got MLE (mem. limit exceeded)
    def firstImpl(self, root):
        tree = self.bfs(root)
        targets = [i for i in range(len(tree)) if tree[i] is not None]
        val_max = float("-inf")
        for idx in targets:
            val_max = max(val_max, self.pathSum(idx, tree))
        # a = max([self.pathSum(idx, tree) for idx in targets])
        return val_max


    def pathSum(self, i, tree):
        toCheck = [(i, tree[i])]
        val_max = tree[i]
        visited = set()

        while toCheck:
            q, v = toCheck.pop(0)
            p = (q - 2) / 2 if q % 2 == 0 else (q - 1) / 2

            if p >= 0 and tree[p] is not None and p not in visited:
                val_max = max(val_max, v + tree[p])
                toCheck.append((p, v + tree[p]))
            l = 2 * q + 1
            if l < len(tree) and tree[l] is not None and l not in visited:
                val_max = max(val_max, v + tree[l])
                toCheck.append((l, v + tree[l]))
            r = 2 * q + 2
            if r < len(tree) and tree[r] is not None and r not in visited:
                val_max = max(val_max, v + tree[r])
                toCheck.append((r, v + tree[r]))
            visited.add(q)
        return val_max


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
