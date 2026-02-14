import tracemalloc

class Node:
    def __init__(self):
        self.related = None

tracemalloc.start()
snapshot1 = tracemalloc.take_snapshot()

# Run some code that creates circular references
a = Node()
b = Node()
a.related = b
b.related = a
del a
del b

snapshot2 = tracemalloc.take_snapshot()
top_stats = snapshot2.compare_to(snapshot1, 'lineno')
print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)
