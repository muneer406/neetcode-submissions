from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        places = defaultdict(list)
        
        for i, x in enumerate(board):
            for j, y in enumerate(x):
                if y != ".":
                    places[y].append([i,j])

        for val, pos in places.items():
            rows, cols, boxes = set(), set(), set()

            for r, c in pos:
                box = (r//3) * 3 + (c//3)

                if r in rows or c in cols or box in boxes:
                    return False
                rows.add(r)
                cols.add(c)
                boxes.add(box)
        
        return True