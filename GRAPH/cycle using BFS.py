from typing import List


class Solution:
    # Function to detect cycle in an undirected graph.
    def bfs(self, start, V, adj, vis):
        q = []
        q.append((start, -1))  # (node,parent)
        vis[start] = 1

        # [(0,-1),()]

        while len(q) != 0:
            node, parent = q.pop(0)

            for nei in adj[node]:

                if vis[nei] == 0:
                    q.append((nei, node))
                    vis[nei] = 1

                elif vis[nei] == 1 and nei != parent:
                    return True

        return False

        def isCycle(self, V: int, adj: List[List[int]]) -> bool:
            # Code here
            vis = [0] * V

            for node in range(V):
                if vis[node] == 0:  # node =4
                    vis[node] = 1  # vis[0]=1  vis[4]=1
                    if self.bfs(node, V, adj, vis):  # [1,1,1,1,1,1,1,1]
                        return True

            return False