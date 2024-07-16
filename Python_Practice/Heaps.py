# Heaps
import heapq

# under the hood they are arrays (aka lists)

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

# Min is always at index 0
print(minHeap[0])
print()

while len(minHeap):
    print(heapq.heappop(minHeap))
print()


# Max Heaps
# Python has no max heaps by default , work around is
# push and pop by -1

maxHeap = []

heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -1)
heapq.heappush(maxHeap, -4)

# Max will be at index 0
print(-1 * maxHeap[0])
print()

while len(maxHeap):
    print(-1 * heapq.heappop(maxHeap))
print()


# Build Heap from inital values (linear time ( O(n)) )
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))
print()
