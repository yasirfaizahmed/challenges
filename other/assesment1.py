from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for i, num in enumerate(nums):
            if i == 0:
                output.append(num**2)
                continue
            if num**2 > output[-1]:
                output.append(num ** 2)
            else:
                j = 0
                while num**2 > output[j]:
                    j += 1
                output.insert(j, num**2)
        return output


print(Solution().sortedSquares([-4,-1,0,3,10]))