from collections import deque

queue = deque()

queue.append("A")
queue.append("B")
queue.append("c")

print(queue.popleft())