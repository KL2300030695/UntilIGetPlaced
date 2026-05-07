class Solution(object):
    def isAnagram(self, s, t):
        s_so=sorted(s)
        t_so=sorted(t)
        if s_so==t_so:
            return True
        return False