from typing import List


class Solution:

    def dfs(self, node, parent, adj, vis):
        vis[node] = 1

        for nei in adj[node]:

            if vis[nei] == 0:
                vis[nei] = 1
                if self.dfs(nei, node, adj, vis):
                    return True

            elif vis[nei] == 1 and parent != nei:
                return True

        return False

        # Function to detect cycle in an undirected graph.
        def isCycle(self, V: int, adj: List[List[int]]) -> bool:
            # Code here
            vis = [0] * V

            for node in range(V):
                if vis[node] == 0:
                    vis[node] = 1
                    if self.dfs(node, -1, adj, vis):
                        return True

            return False