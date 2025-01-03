class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        visited = [False] * len(rooms)
        keys = deque()

        visited[0] = True
        keys.append(rooms[0])

        while keys:
            cur = keys.popleft()
            for key in cur:
                if not visited[key]:
                    keys.append(rooms[key])
                    visited[key] = True

        for room in visited:
            if not room:
                return False

        return True
