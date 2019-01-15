# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
    from BinaryTree.solM863DistanceKinBT import Solution
    root, target, K = Solution().constructCase()
    # root, target, K = Solution().constructCase2()
    Solution().printTree(root)
    ans = Solution().distanceK(root,target,K)
    print("ans: {}".format(ans))
"""


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        import collections
        def dfs(root, d):
            if not root:
                return
            if d == 0:
                res.append(root.val)
                return
            if root.left:
                dfs(root.left, d - 1)
            if root.right:
                dfs(root.right, d - 1)

        parent = {}
        q = collections.deque([root])
        while q:
            u = q.popleft()
            if u == target:
                break
            if u.left:
                parent[u.left] = u
                q.append(u.left)
            if u.right:
                parent[u.right] = u
                q.append(u.right)

        res = []
        trav = target
        d = K
        while trav != root and d > 0:
            tmp = parent[trav]
            d -= 1
            if d == 0:
                res.append(tmp.val)
                break
            if tmp.left == trav:
                dfs(tmp.right, d - 1)
            else:
                dfs(tmp.left, d - 1)
            trav = tmp
        dfs(target, K)
        return res



    def firstImpl(self, root, target, K):
        if target is None:
            return None

        if K == 0:
            return [target.val]

        neighbors = {}
        self.DFS(root, neighbors)
        toCheck = [(target.val, 0)]
        visited = {target.val}
        basket = []
        while toCheck:
            node, distance = toCheck.pop(0)
            if node not in neighbors:
                continue
            if distance >= K:
                break
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    toCheck.append((neighbor, distance + 1))
                    if distance + 1 == K:
                        basket.append(neighbor)
                visited.add(neighbor)
        return basket


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

    # [3,5,1,6,2,0,8,N,N,7,4], node = 5, K = 2
    def constructCase(self):
        from customDataType import TreeNode
        root = TreeNode(3)
        root.left = TreeNode(5)
        root.left.left = TreeNode(6)
        root.left.right = TreeNode(2)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(4)
        root.right = TreeNode(1)
        root.right.left = TreeNode(0)
        root.right.right = TreeNode(8)
        return root, root.left, 2

    # [0,1,N,N,2,N,3,N,4], node = 3, K = 0
    def constructCase2(self):
        from customDataType import TreeNode
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.left.right = TreeNode(2)
        root.left.right.right = TreeNode(3)
        root.left.right.right.right = TreeNode(4)
        return root, root.left.right.right, 0

    @staticmethod
    def printTree(root):
        from customDataType import TreeNode
        TreeNode.printTree(root)