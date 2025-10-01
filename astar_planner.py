import heapq

def astar(grid, start, goal):
    """
    grid: 0=free, 1=obstacle
    start/goal: (r,c)
    """
    R, C = len(grid), len(grid[0])
    def h(a, b):  # 曼哈顿距离
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    open_set = [(h(start, goal), 0, start, None)]
    came_from = {}
    g = {start: 0}
    seen = set()

    while open_set:
        _, cost, cur, parent = heapq.heappop(open_set)
        if cur in seen:
            continue
        seen.add(cur)
        came_from[cur] = parent

        if cur == goal:
            path = []
            node = cur
            while node is not None:
                path.append(node)
                node = came_from[node]
            return list(reversed(path))

        r, c = cur
        for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 0:
                ng = cost + 1
                if (nr, nc) not in g or ng < g[(nr, nc)]:
                    g[(nr, nc)] = ng
                    f = ng + h((nr, nc), goal)
                    heapq.heappush(open_set, (f, ng, (nr, nc), cur))

    return None

if __name__ == "__main__":
    grid = [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [0,1,0,0,0],
        [0,0,0,0,0],
    ]
    print("Path:", astar(grid, (0,0), (4,4)))
