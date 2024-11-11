# Using a list as a queue
from collections import deque

queue = deque()
queue.append(1)  # Enqueue
queue.append(2)
queue.append(3)
print(queue)  # Output: deque([1, 2, 3])

queue.popleft()  # Output: 1 (removes the first item)
print(queue)  # Output: deque([2, 3])
