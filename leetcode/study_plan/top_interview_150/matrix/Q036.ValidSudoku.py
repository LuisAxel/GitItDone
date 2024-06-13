class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        num = ""
        # Check cols
        for x in range(9):
            seen = set()
            for y in range(9):
                num = board[x][y]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # Check cols
        for x in range(9):
            seen = set()
            for y in range(9):
                num = board[y][x]
                if num == '.':
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # Check box
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        num = board[(3 * box_row) + x][(3 * box_col) + y]
                        if num == '.':
                            continue
                        if num in seen:
                            return False
                        seen.add(num)
        return True
