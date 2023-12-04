from collections import namedtuple
import heapq
from queue import PriorityQueue
from typing import Optional


with open('./advent12.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# part 1

Location = namedtuple("Location", "x y z")

class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[float, Location]] = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item: Location, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self) -> Location:
        return heapq.heappop(self.elements)[1]

class Graph:
    def __init__(self, grid):
        self.height = len(grid[0])
        self.width = len(grid)
        self.grid = grid
        self.alphabet = "SabcdefghijklmnopqrstuvwxyzE"
        self.start = self.find('S')
        self.end = self.find('E')

    def in_bounds(self, id: Location):
        return 0 <= id.x < self.width and 0 <= id.y < self.height
    
    def neighbors(self, id: Location):
        (x, y, z) = id
        neighbors = [Location(x+1, y, 0), Location(x-1, y, 0), Location(x, y-1, 0), Location(x, y+1, 0)]
        results = filter(self.in_bounds, neighbors)
        locs = []
        for r in results:
            if self.alphabet.index(self.grid[r.x][r.y]) - z < 2:
                locs.append(self.grid[r.x][r.y])
        return locs

    def find(self, char):
        for i, string in enumerate(grid):
            for j, c in enumerate(string):
                if c == char:
                    return Location(i, j, self.alphabet.index(char))
        return None

    def heuristic(self, a: Location, b: Location) -> float:
        (x1, y1, z1) = a
        (x2, y2, z2) = b
        return abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
    
    def a_star_search(self, graph, start: Location, goal: Location):
        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from: dict[Location, Optional[Location]] = {}
        cost_so_far: dict[Location, float] = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            current: Location = frontier.get()
            if current == goal:
                break
            
            for next in graph.neighbors(current):
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    print(next)
                    priority = new_cost + self.heuristic(next, goal)
                    frontier.put(next, priority)
                    came_from[next] = current
        return came_from, cost_so_far

if __name__ == "__main__":
    grid = [['' for _ in range(len(content))] for _ in range(len(content[0]))]

    # Iterate over the content
    for i, string in enumerate(content):
        # Iterate over the characters in the string
        for j, char in enumerate(string):
            # Replace the character in the grid with the character from the content
            grid[j][i] = char

    graph = Graph(grid)
    came_from, cost_so_far = graph.a_star_search(graph, graph.start, graph.end)
    print(cost_so_far[graph.end])