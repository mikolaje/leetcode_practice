# coding=u8

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D"],
    "F": ["E"]
}

area = {
    (0, 0): [(0, 1), (1, 0)]
}
grid = [[]]
def area_dfs(x, y):
    queue = []
    queue.append((x,y))
    seen = set()
    if grid[x][y]==1 or grid[x+1][y]==1 or grid[x][y+1]==1 or grid[x-1][y]==1:
        return 1
    else:
        return 0


def dfs(graph, start):
    queue = []
    queue.append(start)
    seen = set()
    seen.add(start)
    while queue:
        vertex = queue.pop()   # 以stack 的方式
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)

dfs(graph, 'A')

