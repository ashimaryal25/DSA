class Solution(object):

  def maxAreaOfIsland(self, grid):
    maxArea = 0  # Start at 0 instead of -inf
    r = len(grid)
    c = len(grid[0])
    visited = set()

    def dfs(grid, row, col):
      # Bounds check first, then water and visited checks
      if (
          row < 0
          or row >= r
          or col < 0
          or col >= c
          or grid[row][col] == 0
          or (row, col) in visited
      ):
        return 0

      visited.add((row, col))

      a1 = dfs(grid, row + 1, col)
      a2 = dfs(grid, row - 1, col)
      a3 = dfs(grid, row, col + 1)
      a4 = dfs(grid, row, col - 1)

      # Add 1 (this cell) + all 4 branches
      return 1 + a1 + a2 + a3 + a4

    for i in range(r):
      for j in range(c):
        if grid[i][j] == 1 and (i, j) not in visited:
          # Capture the returned area
          maxArea = max(maxArea, dfs(grid, i, j))

    return maxArea

        