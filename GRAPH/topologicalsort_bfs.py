class Solution:

    # Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0] * V

        for node in range(V):  # node =0,1,2,..
            for nei in adj[node]:  # node ----> nei # 2--->0 (nei)
                indegree[nei] += 1

        q = []

        for node in range(V):
            if indegree[node] == 0:
                q.append(node)

        ans = []

        while len(q) != 0:
            node = q.pop(0)
            ans.append(node)

            for nei in adj[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        # print(ans)
        return ans