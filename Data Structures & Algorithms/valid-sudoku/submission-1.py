class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            count = [0]*9
            for c in range(9):
                char = board[r][c]
                if char == ".": continue
                i = int(char)
                count[i-1] += 1
                if count[i-1] > 1: return False
        
        for c in range(9):
            count = [0]*9
            for r in range(9):
                char = board[r][c]
                if char == ".": continue
                i = int(char)
                count[i-1] += 1
                if count[i-1] > 1: return False
        
        for br in range(3):
            for bc in range(3):
                count = [0]*9
                for i in range(3):
                    for j in range(3):
                        char = board[br * 3 + i][bc * 3 + j]
                        if char == ".": continue
                        i2 = int(char)
                        count[i2-1] += 1
                        if count[i2-1] > 1:
                            return False
        
        return True