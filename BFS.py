from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    visited.add(start)

    while queue:
        node = queue.popleft()
        order.append(node)
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append(neigh)
    return order


def bfs_shortest_path(graph, start, target):
    visited = set([start])
    parent = {start: None}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == target:
            break
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                parent[neigh] = node
                queue.append(neigh)

    if target not in parent:
        return None

    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path


print("---- BFS LAB PROGRAM ----")

n = int(input("Enter number of nodes: "))
print("Enter node labels:")
labels = input().split()

graph = {node: [] for node in labels}

m = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(m):
    u, v = input().split()
    graph[u].append(v)

start = input("Enter start node: ")
target = input("Enter target for shortest path: ")

print("BFS Traversal:", bfs_traversal(graph, start))

path = bfs_shortest_path(graph, start, target)
if path is None:
    print("No path exists")
else:
    print("Shortest Path:", " -> ".join(path))
    print("Edges:", len(path) - 1)
