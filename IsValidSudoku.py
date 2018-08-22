class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=[{},{},{},{},{},{},{},{},{}]
        col=[{},{},{},{},{},{},{},{},{}]
        box=[{},{},{},{},{},{},{},{},{}]
        for i in range(9):
            for j in range(9):
                num=(i//3)*3+j//3
                if board[i][j]!='.':
                    temp=board[i][j]
                    if board[i][j] not in row[i] and board[i][j] not in col[j] and board[i][j] not in box[num]:
                        row[i][temp]=1
                        col[j][temp]=1
                        box[num][temp]=1
                    else:
                        return False
        return True
