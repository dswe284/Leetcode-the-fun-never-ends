
# Leetcode 675. Cut Off Trees for Golf Event
# Hard 1/19/21

# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:

#     0 means the cell cannot be walked through.
#     1 represents an empty cell that can be walked through.
#     A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.

# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.

# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).

# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.

# You are guaranteed that no two trees have the same height, and there is at least one tree needs to be cut off.



from collections import defaultdict
import heapq

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        N, M, MAX = len(forest), len(forest[0]) if len(forest) else 0, float('inf')
        
        def get(frX: int, frY: int, toX: int, toY: int) -> int: # get shortest
            if not (0 <= frX < N and 0 <= toX < N and 0 <= frY < M and 0 <= toY < M):
                return MAX
            if not forest[frX][frY]:
                return MAX
            
            # queue = [ (estimated total length, estimated remaining length, distance from source, source X, source Y) ]
            queue = [(abs(frX-toX)+abs(frY-toY), abs(frX-toX)+abs(frY-toY), 0, frX, frY  )]
            shortest = defaultdict(lambda: MAX)
            shortest[frX, frY] = 0
            
            while len(queue):
                est, remain, d, x, y = heapq.heappop(queue)
                if (x, y) == (toX, toY):
                    return d
                for a, b in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                    remaining = abs(a-toX) + abs(b-toY)
                    if 0 <= a < N and 0 <= b < M and forest[a][b] and shortest[a, b] > d+1:
                        shortest[a, b] = d+1
                        heapq.heappush(queue, (remaining+d+1, remaining, d+1, a, b) )
            
            return MAX
        
        path = sorted( (forest[x][y], x, y) for x in range(N) for y in range(M) if forest[x][y] > 1 )

        ans, frX, frY = 0, 0, 0
        for v, x, y in path:
            s = get(frX, frY, x, y)
            if s < MAX:
                ans, frX, frY = ans + s, x, y
            else:
                return -1
        return ans