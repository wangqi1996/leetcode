class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        record = {}

        def match(s, p):
            if s in record and p in record[s]:
                return False
            s_index = 0
            s_len = len(s)
            p_len = len(p)
            for p_index, pp in enumerate(p):
                if pp == '*':
                    while s_index < s_len:
                        if self.isMatch(s[s_index:], p[p_index + 1:]):
                            return True
                        else:
                            record.setdefault(s[s_index:], [])
                            record[s[s_index:]].append(p[p_index + 1:])
                            if p[p_index - 1] == '.' or (p[p_index - 1] == s[s_index]):
                                s_index += 1
                            else:
                                return False

                    if s_index == s_len and p_index + 1 == p_len:
                        return True
                    else:
                        return False
                elif p_index < p_len - 1 and p[p_index + 1] == '*':
                    continue
                elif s[s_index] != p[p_index] and p[p_index] != '.':
                    return False
                else:
                    s_index += 1

            if s_index == s_len:
                return True
            else:
                return False

        return match(s, p)


if __name__ == '__main__':
    print(Solution().isMatch("aaaa", "aaa") is False)
    print(Solution().isMatch("a", "ab*") is True)
    print(Solution().isMatch("ab", ".*c") is False)
    print(Solution().isMatch("aa", "a*") is True)
    print(Solution().isMatch("aa", "a") is False)
    print(Solution().isMatch("ab", ".*") is True)
    print(Solution().isMatch("aab", "c*a*b*") is True)
    print(Solution().isMatch("mississippi", "mis*is*p*.") is False)
    print(Solution().isMatch("", "") is True)
    print(Solution().isMatch(" ", " *") is True)
    print(Solution().isMatch("issippi", "is*ip*.") is True)
    print(Solution().isMatch("ippi", "ip*.") is True)
