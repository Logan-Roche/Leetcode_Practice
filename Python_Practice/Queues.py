# Queues (double ended queue)
# Benifit is all operations are done in constant time

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)

queue.popleft()

print(queue)

queue.appendleft(1)
print(queue)
