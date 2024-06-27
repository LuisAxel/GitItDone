class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Obstacle at start or end
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        paths = [[0 for _ in range(cols)] for __ in range(rows)]
        paths[0][0] = 1

        for col in range(1, cols):
            if obstacleGrid[0][col] == 1:
                break
            paths[0][col] = 1

        for row in range(1, rows):
            if obstacleGrid[row][0] == 1:
                break
            paths[row][0] = 1

        for row in range(1, rows):
            for col in range(1, cols):
                if obstacleGrid[row][col] != 1:
                    paths[row][col] = paths[row - 1][col] + paths[row][col - 1]

        return paths[-1][-1]
