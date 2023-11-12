class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        prereq = {}

        for i in range(numCourses):
            prereq[i] = []
        
        # Populate the adjacency list
        for pre in prerequisites:
            prereq[pre[0]].append(pre[1])
        
        output = []

        visit = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visit:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return output

        
        