from typing import List
from queue import Queue


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        q = []
        q.append(0)

        visited = [0] * V  # [1,0,0,0,0]
        visited[0] = 1
        ans = []

        while len(q) != 0:
            node = q.pop(0)
            ans.append(node)

            for nei in adj[node]:
                if visited[nei] == 0:
                    q.append(nei)
                    visited[nei] = 1

        return ans
