class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0

        previous = None

        for i in range(len(nums)):
            if (nums[i] != previous):
                nums[k] = nums[i]
                k += 1

            previous = nums[i]
            
        return k

            
        