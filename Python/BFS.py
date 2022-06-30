from collections import deque
def BFS(graph, start, visited):
    queue = deque([start]) #큐 생성

    visited[start] = True

    while queue:

        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if visited == False:
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

BFS(graph, 1, visited)