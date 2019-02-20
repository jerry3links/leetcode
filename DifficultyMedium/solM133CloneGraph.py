"""
    from DifficultyMedium.solM133CloneGraph import Solution
    node = Solution().testCase()
    ans = Solution().cloneGraph(node)
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):

        if node is None:
            return None

        root = None

        visited = set()
        initial = True
        cloneMap = {}

        queue = [node]
        while queue:
            target = queue.pop(0)

            if target in cloneMap:
                parent = cloneMap[target]
            else:
                parent = UndirectedGraphNode(target.label)
                cloneMap[target] = parent

            if target not in visited:
                visited.add(target)
                if initial:
                    root = parent
                    initial = False

            for n in target.neighbors:
                if n in cloneMap:
                    child = cloneMap.get(n)
                else:
                    child = UndirectedGraphNode(n.label)
                    cloneMap[n] = child
                parent.neighbors.append(child)
                if n not in visited and n not in queue:
                    queue.append(n)

        return root


    def testCase(self):
        # {0,1,2 # 1,2 # 2,2}
        node2 = UndirectedGraphNode(2)
        node2.neighbors.append(node2)
        node1 = UndirectedGraphNode(1)
        node1.neighbors.append(node2)
        node0 = UndirectedGraphNode(0)
        node0.neighbors.append(node1)
        node0.neighbors.append(node2)
        return node0

    def testCase2(self):
        # {0,0,0}
        node0 = UndirectedGraphNode(0)
        node0.neighbors.append(node0)
        node0.neighbors.append(node0)
        return node0


    def printNode(self, node):
        print("[{}]".format(node.label))
        for n in node.neighbors:
            print("->[{}]".format(n.label))

    def printGraph(self, node):
        queue = [node]
        visited = set()
        while queue:
            tmp = queue.pop(0)
            if tmp not in visited:
                visited.add(tmp)
                print("visit node [{}] ...".format(tmp.label))
                self.printNode(tmp)

            for n in tmp.neighbors:
                if n not in visited:
                    queue.append(n)
