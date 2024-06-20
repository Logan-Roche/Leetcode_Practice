class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for outer in range(len(nums)):
            for inner in range(1, len(nums)):
                if nums[outer] + nums[inner] == target and (inner != outer):
                    return str(outer) + str(inner)