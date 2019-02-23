import queue

q = queue.Queue()

q.put("Hello")
q.put("World")

for item in range(q.qsize()):
    print(q.get())

print(q.empty())
