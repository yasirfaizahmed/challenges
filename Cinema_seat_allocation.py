# flake8: noqa
from typing import List

class Solution:
  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    output = 0
    
    in_same_row = [[] for _ in range(n)]
    for reserved in reservedSeats:
      in_same_row[reserved[0] - 1].append(reserved[1])

    for row in in_same_row:
      if len(row) == 0:
        output += 2
        continue
      if all([col < 4 or col > 7 for col in row]):    # no one in middle
        if all([col == 1 or col == 10 for col in row]):   # taken only at edges
          output += 2
          continue
        else:
          output += 1
          continue

      if all(col in [1,2,3,4,5] for col in row):
        output += 1
        continue
      elif all(col in [6,7,8,9,10] for col in row):
        output += 1
        continue
      elif all(col not in [2,3,4,5] for col in row):
        output += 1
        continue
      elif all(col not in [6,7,8,9] for col in row):
        output += 1
        continue


    return output
      # else:
      #   if col == 1 or col == 10:
      #     output += 2
      #     continue
        # elif col > 1 and col < 4


Solution().maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])