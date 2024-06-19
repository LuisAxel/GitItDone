class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [[] for _ in range(numCourses)]
        prereq = [0] * numCourses

        # req[i] = Classes that need i
        for a, b in prerequisites:
            req[b].append(a)

        # prereq[i] = Number of classes that i needs
        for a, b in prerequisites:
            prereq[a] += 1

        can_take = []

        # We start with a classes that doesnt need other classes
        for a in range(numCourses):
            if prereq[a] == 0:
                can_take.append(a)

        ans = []

        # While we can take classes
        while can_take:
            course = can_take.pop()
            ans.append(course)

            # remove this requisite from other classes
            for need in req[course]:
                prereq[need] -= 1
                if prereq[need] == 0:
                    can_take.append(need)

        return ans if len(ans) == numCourses else []
