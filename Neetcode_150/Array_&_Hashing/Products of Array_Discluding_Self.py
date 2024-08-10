class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productList = []

        for i in range(len(nums)):
            if nums[i] == 0:
                product = 1
            else:
                product = nums[i]
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            if nums[i] == 0:
                productList.append(product)
            else:
                product = product // nums[i]
                productList.append(product)
        return productList