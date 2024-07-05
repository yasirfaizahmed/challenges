from typing import List
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ""
        for sub_s in order:
            if sub_s in s:
                output += sub_s
            s.pop()


print(Solution().customSortString(order="bcafg", s="abcd"))