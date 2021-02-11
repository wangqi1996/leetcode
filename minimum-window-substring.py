class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) <= 1:
            if t == s:
                return t
            return ""

        mark = {}
        mark_start = {}
        for tt in t:
            mark[tt] = []
            mark_start[tt] = []

        # init

