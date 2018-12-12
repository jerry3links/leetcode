"""
    from DifficultyMedium.sol785IsBipartite import Solution
    graph = [[1,3], [0,2], [1,3], [0,2]]
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    ans = Solution().isBipartite(graph)
    print(ans)
"""


class Solution:

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        colors = [-1 for i in graph]
        for v in range(len(graph)):
            if colors[v] == -1:
                colors[v] = 0
                if self.sameOccur(v, graph, colors):
                    return False
        return True

    def sameOccur(self, v, graph, colors):
        for w in graph[v]:
            if colors[w] == -1:
                colors[w] = int(not colors[v])
                if self.sameOccur(w, graph, colors):
                    return True
            else:
                if colors[w] == colors[v]:
                    return True
        return False
