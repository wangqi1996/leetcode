class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        s_dict, p_dict = {}, {}
        for pp in p:
            p_dict.setdefault(pp, 0)
            s_dict.setdefault(pp, 0)
            p_dict[pp] += 1
        distance = 0
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []
        for i in range(len_p):
            if s[i] in p:
                s_dict[s[i]] += 1
                if s_dict[s[i]] <= p_dict[s[i]]:
                    distance += 1
        result = [0] if distance == len_p else []
        for i in range(len_p, len_s):
            start = i - len_p
            if s[start] in p_dict:
                s_dict[s[start]] -= 1
                if s_dict[s[start]] < p_dict[s[start]]:
                    distance -= 1
            if s[i] in p_dict:
                s_dict[s[i]] += 1
                if s_dict[s[i]] <= p_dict[s[i]]:
                    distance += 1
            if distance == len_p:
                result.append(start + 1)
        return result


if __name__ == '__main__':
    print(Solution().findAnagrams("cbaebabacd", "abc"))
