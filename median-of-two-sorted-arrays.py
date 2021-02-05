class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i, j, _len1, _len2 = 0, 0, len(nums1), len(nums2)
        if _len1 == 0:
            _len1, nums1 = _len2, nums2
            if _len1 % 2 != 0:
                return nums1[_len1 // 2]
            else:
                return (nums1[_len1 // 2] + nums1[_len1 // 2 - 1])*1.0 / 2
        mid = (_len1 + _len2 - 1) // 2
        index = 0
        while index < mid:
            if i < _len1 and j < _len2:
                if nums1[i] < nums2[j]:
                    i += 1
                else:
                    j += 1
            elif i < _len1:
                i += 1
            else:
                j += 1
            index += 1

        def get_next_value(i, j):
            if i < _len1 and j < _len2:
                if nums1[i] < nums2[j]:
                    return nums1[i], 1, 0
                else:
                    return nums2[j], 0, 1
            elif i < _len1:
                return nums1[i], 1, 0
            else:
                return nums2[j], 0, 1

        value, t1, t2 = get_next_value(i, j)
        i += t1
        j += t2
        need_average = (_len1 + _len2) % 2
        if not need_average:
            v2, _, _ = get_next_value(i, j)
            value = (v2 + value)*1.0 / 2

        return value


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    print(Solution().findMedianSortedArrays([0, 0], [0, 0]))
    print(Solution().findMedianSortedArrays([], [2]))
    print(Solution().findMedianSortedArrays([2], []))
    print(Solution().findMedianSortedArrays([2, 3], []))
