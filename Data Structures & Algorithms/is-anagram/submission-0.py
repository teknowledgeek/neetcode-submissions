class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t :
            return True

        if not s or not t:
            return False

        if len(s) != len(t):
            return False
        else:
            i=0
            while i < len(t):

                if t[i] in s:
                    s=s.replace(t[i],"",1)
                else :
                    return False
                i += 1

        return True