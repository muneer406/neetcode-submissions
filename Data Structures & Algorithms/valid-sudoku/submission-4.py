class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nums = [0]*9
            for col in range(9):
                val = board[row][col]
                if val == ".": continue
                nums[int(val)-1] += 1
                if nums[int(val)-1] > 1: return False                
                
        for col in range(9):
            nums = [0]*9
            for row in range(9):
                val = board[row][col]
                if val == ".": continue
                nums[int(val)-1] += 1
                if nums[int(val)-1] > 1: return False                
                
        for br in range(3):
            for bc in range(3):
                nums = [0]*9
                for i in range(3):
                    for j in range(3):
                        val = board[br*3 + i][bc*3 + j]
                        if val == ".": continue
                        nums[int(val)-1] += 1
                        if nums[int(val)-1] > 1: return False                
                
        return True