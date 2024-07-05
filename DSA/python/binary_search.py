from typing import List

class Search():
  # returns index of the target if found
  # -1 -> target does not exists
  def solve(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
      mid = low + (high - low)//2
      if nums[mid] == target:
        return mid
      elif target < nums[mid]:
        high = mid - 1
      else:
        low = mid + 1
    return -1
      
      


print(Search().solve([-1,0,3,5,9,12], 9))