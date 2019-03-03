# coding=u8

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["E"]
}



def bfs(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while queue:
        vertex = queue.pop(0)   # 以 queue 的方式
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

dfs(graph, 'A')

