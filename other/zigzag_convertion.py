# flake8: noqa
class Solution:
  def convert(self, s: str, numRows: int) -> str:

    # cal num of cols required
    numCols = 0
    idx = 0
    while idx < len(s):
      for _ in range(numRows):
        if idx < len(s):
          idx += 1

      numCols += 1
      for _ in range(numRows - 2):
        if idx < len(s):
          idx += 1
          numCols += 1

    
    matrix = []
    for i in range(numRows):
      row = []
      for j in range(numCols):
        row.append(0)
      matrix.append(row)

    
    for i in range(numCols):
      for j in range(numRows):
        if # TODO
    
    print(matrix)


Solution().convert("PAYPALISHIRING", 4)