class Solution:

    def helper(self, node, adj, ans, visited):
        ans.append(node)  # [0,1]
        visited[node] = 1  # [ 1,1,0,0,0]

        for nei in adj[node]:  # nei =1,2,3 nei=4,5
            if visited[nei] == 0:  # unvisted
                self.helper(nei, adj, ans, visited)

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        visited = [0] * V
        ans = []

        self.helper(0, adj, ans, visited)
        return ans