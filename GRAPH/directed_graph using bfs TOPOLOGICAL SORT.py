class Solution:
    def canFinish(self, nc: int, prerequisites: List[List[int]]) -> bool:
        # 1. Create a Graph ie adjaceny list
        adj = defaultdict(list)
        for u, v in prerequisites:
            # in order to complete course u, first complete course v
            adj[v].append(u)
        print(adj)
        # Now Apply Topological Sorting(BFS) -- O(v+e)/O(v)
        # Using Topological Sorting check whether there is a cycle in graph or not
        # if cycle: return false (courses cant be done)
        # else: return True (courses can be done)

        # 2. find indegree
        indegree = [0] * nc
        for i in range(nc):
            for nei in adj[i]:
                indegree[nei] += 1
        print(indegree)
        # 3. Insert all nodes in queue which have indegree 0
        q = []
        for node in range(nc):
            if indegree[node] == 0:
                q.append(node)

        courses = []
        while len(q) != 0:
            course = q.pop(0)
            courses.append(course)

            for neig in adj[course]:
                indegree[neig] -= 1

                if indegree[neig] == 0:
                    q.append(neig)

        print(indegree)

        if len(courses) == nc:
            # no cycle ie all courses can be completed
            print("Courses Completed", courses)
            return True
        else:
            # cycle present ie all course cannot be completed
            return False