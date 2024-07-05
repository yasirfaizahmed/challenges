# flake8: noqa

class Solution:

  def check_pseudo_palindrome(self, string: str) -> bool:
    char_map = [0] * 256        # empty 0 map
    pair = enumerate(string)
    for i, char in pair:
      char_map[ord(char)] += 1    # increment the position where the char recides
    
    odds = 0
    for cnt in char_map:
      if cnt % 2 == 1:
        odds += 1
      
    if odds > 1:
      return False
    return True

  def check_palindrome(self, string: str) -> bool:
    str_len = len(string)
    if str_len == 1:
      return True
    is_palindrome = False
    for i in range(str_len // 2):
      if string[i] == string[str_len - 1 - i]:
        is_palindrome = True
      else:
        is_palindrome = False
        break
    return is_palindrome

  def longestPalindrome(self, s: str) -> str:
      if len(s) <= 1:
          return s

      def expand_from_center(left, right):
          while left >= 0 and right < len(s) and s[left] == s[right]:
              left -= 1
              right += 1
          return s[left + 1:right]

      max_str = s[0]

      for i in range(len(s) - 1):
          odd = expand_from_center(i, i)
          even = expand_from_center(i, i + 1)

          if len(odd) > len(max_str):
              max_str = odd
          if len(even) > len(max_str):
              max_str = even

      return max_str


print(Solution().longestPalindrome("babad"))