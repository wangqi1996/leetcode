class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            t = list(s)
            t.sort()
            ss = ''.join(t)
            result.setdefault(ss, [])
            result[ss].append(s)

        return list(result.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
