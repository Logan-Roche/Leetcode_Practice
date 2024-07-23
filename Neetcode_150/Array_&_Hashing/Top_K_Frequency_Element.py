class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq

        hashMap = {}
        heap = []
        result = []

        for i in nums:
            hashMap[i] = hashMap.get(i, 0) + 1

        print(hashMap)

        for key in hashMap.values():
            heapq.heappush(heap, key * -1)
        
        print(heap)

        while (k > 0):
            temp = heapq.heappop(heap)
            for key, val in hashMap.items():
                if temp * -1 == val:
                    result.append(key)
                    hashMap[key] = -1
            k -= 1
        return result
        
        
        