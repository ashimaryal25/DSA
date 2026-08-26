from collections import deque

#cur is the advanced class that has requirements, while preq is the prerequisite (the key)
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        
        #bfs approach
        locked = [0] * numCourses

        unlock = { i : [] for i in range(numCourses)}

        #preq var is the class that has prerequisites

        for cur,preq in prerequisites:

            unlock[preq].append(cur)

            locked[cur] += 1


        q = deque()

        for i in range(numCourses):

            if locked[i] == 0 :
                q.append(i)
                
        res = []  

        while q:

            cur = q.pop()

            res.append(cur)
            
            for course in unlock[cur]:

                locked[course] -= 1

                if locked[course] == 0:
                    q.append(course)


        if len(res) != numCourses:
            return []
        return res    

