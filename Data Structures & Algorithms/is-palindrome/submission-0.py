import re
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s is None:
            return True

        s = re.sub(r'[^A-Za-z0-9]', "", s)
        s = s.lower()

        def expand_from_middle(left_index, right_index):

            while left_index >=0 and right_index < len(s):

                if s[left_index] == s[right_index]:
                    left_index -= 1
                    right_index += 1
                else:
                    return False
            return True

        if len(s) // 2 == len(s) / 2:

            left_index = len(s)// 2 -1
            right_index = len(s) // 2

        else :
            left_index = len(s)// 2 
            right_index = len(s) // 2

        return expand_from_middle(left_index, right_index)