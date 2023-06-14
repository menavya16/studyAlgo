class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = [0]
        for i in range(len(nums)):
            new.append(nums[i] + new[i])
        return new[1:]

