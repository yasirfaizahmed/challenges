# flake8: noqa
from typing import Optional

class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 1:
      return 1
    sub_str_list = []
    sub_str = ""
    for idx, char in enumerate(s):
      if char not in sub_str:

        # check the sub_str is continious
        sub_str_idx = len(sub_str) - 1
        i = idx - 1
        con = False
        while sub_str_idx != -1:
          if sub_str[sub_str_idx] == s[i]:
            sub_str_idx -= 1
            i -= 1
          else:
            con = False
            break
          con = True

        if con or idx == 0:
          sub_str += char
          if idx + 1 == len(s):
            sub_str_list.append(sub_str)
      else:
        sub_str_list.append(sub_str)
        sub_str = sub_str.split(char)[1] + char if len(sub_str) > 1 else char

    final_l = []
    for l in sub_str_list:
      final_l.append(len(l))

    try:
      return max(final_l)
    except Exception:
      return 0
  
print(Solution().lengthOfLongestSubstring("dvdf"))