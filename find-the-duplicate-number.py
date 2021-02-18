class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        slow = nums[slow]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return slow


if __name__ == '__main__':
    print(Solution().findDuplicate([3, 1, 3, 4, 2]))
