class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        mySet = set(nums)

        longest = 0

        for n in mySet:
            if(n - 1) not in mySet:
                length = 1

                while(n + length) in mySet:
                    length += 1
                
                longest = max(length, longest)
        return longest
        
        