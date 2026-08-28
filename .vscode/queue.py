from collections import deque
dq=deque()
dq.append(10)
dq.append(20)
dq.append(30)
dq.appendleft(40)
print(dq)
print(dq.pop()) #right
print(dq.popleft()) #del left
