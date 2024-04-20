'''class Solution:
    def canFinish(self, numCourses: int, prerequisites:int) -> bool:
        child =collections.defaultdict(list)
        branch = [0] * numCourses
        for i, j in prerequisites:
            child[j].append(i)
            branch[i] += 1
        q = collections.deque()
        for i in range(numCourses):
            if branch[i] == 0:
                q.append(i)
        

        while q:
            node=q.popleft()
            for i in child[node]:
                branch[i]-=1
                if branch[i]==0:
                    q.append(i)
        for i in branch:
            if i != 0:
                return False
        return True'''


class Solution:
    def canFinish(self, numCourses: int, prerequisites:int) -> bool:
        def dfs(course):
            if visited[course] == 1:
                return False
            if visited[course] == -1:
                return True

            visited[course] = 1
            for next_course in child[course]:
                if not dfs(next_course):
                    return False
            visited[course] = -1
            return True
        
        # Build the child dictionary representing the graph
        child = collections.defaultdict(list)
        for i, j in prerequisites:
            child[j].append(i)
        
        # Initialize visited status list
        visited = [0] * numCourses
        
        # Start DFS traversal from each unvisited course
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

