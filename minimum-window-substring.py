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

        len_t, _len, left, right = len(t), len(s), 0, 0
        t_window = {}
        s_window = {}
        for i in range(len_t):
            tt = t[i]
            t_window.setdefault(tt, 0)
            t_window[tt] += 1

        distance = 0
        result = s + "."
        while right < _len:
            c = s[right]
            if c not in t:
                right += 1
                continue

            s_window.setdefault(c, 0)
            s_window[c] += 1
            if s_window[c] <= t_window[c]:
                distance += 1
                if distance == len_t:
                    while True:
                        left += 1
                        c = s[left - 1]
                        if c in t:
                            s_window[c] -= 1
                            if s_window[c] < t_window[c]:
                                distance -= 1
                                break
                    if len(s[left - 1:right + 1]) < len(result):
                        result = s[left - 1:right + 1]
            right += 1

        if len(result) == len(s) + 1:
            return ""
        else:
            return result


if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
