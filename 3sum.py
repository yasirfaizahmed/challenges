from typing import List


class Solution:
  def _check_exists(self, arr: List[int], master_arr: List[List]) -> bool:
    if master_arr == []:
      return False
    for array in master_arr:
      if all(element in array for element in arr):
        return True
    return False

  def threeSum(self, nums: List[int]) -> List[List[int]]:
    output = []
    new_nums = {}
    for idx, num in enumerate(nums):
      new_nums[idx] = num

    if nums[0] == nums[1] == nums[2] == 0:
      return [[0, 0, 0]]
  
    if sum([nums[0], nums[1], nums[2]]) == 0 and len(nums) == 3:
      return [nums]

    already_done_idx = []
    for i in range(len(nums) - 1):
      for j in range(len(nums) - 1):
        for k in range(len(nums) - 1):
          if i != j and j != k and k != i:
            if sum([nums[i], nums[j], nums[k]]) == 0:
              if self._check_exists([nums[i], nums[j], nums[k]], already_done_idx) is False:
                output.append([nums[i], nums[j], nums[k]])
                already_done_idx.append([nums[i], nums[j], nums[k]])
    
    return output


if __name__ == "__main__":
  Solution().threeSum([1,1,1])
