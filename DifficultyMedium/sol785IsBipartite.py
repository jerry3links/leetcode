"""
    from DifficultyMedium.sol785IsBipartite import Solution
    graph = [[1,3], [0,2], [1,3], [0,2]]
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
    ans = Solution().isBipartite(graph)
    print(ans)
"""


class Solution:

    G = None

    def isCyclicUtil(self, v, visited, graph):
        visited[v] = True
        for i in graph[v]:
            if visited[i] == False:
                if self.isCyclicUtil(i, visited, graph):
                    return True
        return False


    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        V = [False for v in graph]
        for v in range(len(V)):
            if V[v] == False:
                if self.isCyclicUtil(v, V, graph):
                    return False
        return True
