class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(a):
            nonlocal prereq, seen
            # Can take this class, no requisites
            if not prereq[a]:
                return True

            # Cycle
            if seen[a]:
                return False

            seen[a] = True

            for b in prereq[a]:
                # Cycle
                if not dfs(b):
                    return False

            # Could took all prereq classes
            prereq[a] = []
            return True


        prereq = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            prereq[a].append(b)

        seen = [False] * numCourses

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
