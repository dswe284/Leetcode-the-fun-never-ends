# Leetcode 207. Course Schedule
# Medium 12/29/20

# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0. So it is possible.

# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.

 
#  Constraints:

#     The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
#     You may assume that there are no duplicate edges in the input prerequisites.
#     1 <= numCourses <= 10^5


# Solution 1

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prereq list
        preMap = { i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet = all courses along the curr DFS path
        visitSet = set()
        def dfs(crs):
            if crs in visitSet:
                return False
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True



# Solution 2

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for i, j in prerequisites:
            graph[i].append(j)
            
        def dfs(i, temp_stack):
            if visit[i] == 1:
                return False
            if visit[i] == -1:
                return True
            visit[i] = 1
            
            for node in graph[i]:
                if not dfs(node, temp_stack):
                    return False
            visit[i] = -1
            temp_stack.append(i)
            return True
        
        for i in range(numCourses):
            temp_stack = []
            if not dfs(i, temp_stack):
                return []
            res += temp_stack
        return res
                



# Solution 3

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        res = []
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for i, j in prerequisites:
            graph[i].append(j)
            
        def hasCycle(i, temp_stack):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = 1
            
            for node in graph[i]:
                if hasCycle(node, temp_stack):
                    return True
            visit[i] = -1
            temp_stack.append(i)
            return False
        
        for i in range(numCourses):
            temp_stack = []
            if hasCycle(i, temp_stack):
                return False
        return True
                

# Solution 4

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for i, j in prerequisites:
            graph[i].append(j)
            
        def hasCycle(i):
            if visit[i] == 1:
                return True
            if visit[i] == -1:
                return False
            visit[i] = 1
            
            for node in graph[i]:
                if hasCycle(node):
                    return True
            visit[i] = -1
           # temp_stack.append(i)
            return False
        
        for i in range(numCourses):
           # temp_stack = []
            if hasCycle(i):
                return False
        return True
                