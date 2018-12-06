"""Put the following in demo,py
from tstBinaryTree import treeInstance
tree = treeInstance().createBtree()
from sol103ZigZagBTree.py import Solution
L = Solution().zigzagLevelOrder(tree)
"""



class Solution:

    depthMap = {}

    def pushTree(self, root, d):

        if not root:
            return

        if d in self.depthMap:
            self.depthMap[d].append(root)
        else:
            self.depthMap[d] = [root]

        self.pushTree(root.left, d+1)
        self.pushTree(root.right, d+1)

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        self.pushTree(root, 0)

        depths = self.depthMap.keys()

        L = []
        if not depths:
            return L

        for d in range(0, max(depths) + 1):
            nodeLst = self.depthMap[d]
            if d % 2 == 0:
                l = []
                for i in range(0, len(nodeLst)):
                    l.append(nodeLst[i].val)
                L.append(l)
            else:
                nodeLstR = list(reversed(nodeLst))
                l = []
                for i in range(0, len(nodeLstR)):
                    l.append(nodeLstR[i].val)
                L.append(l)
        self.depthMap.clear()
        return L