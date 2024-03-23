class Solution:

    def dfs(self, node, adj, vis, stack):
        vis[node] = 1

        for nei in adj[node]:
            if vis[nei] == 0:
                self.dfs(nei, adj, vis, stack)

        stack.append(node)

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        vis = [0] * V
        stack = []

        for node in range(V):
            if vis[node] == 0:
                self.dfs(node, adj, vis, stack)

        return stack[::-1]