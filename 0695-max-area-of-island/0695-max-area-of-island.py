class Solution(object):
    #sinking approach turning 1s to 0s instead of using visited set
  def maxAreaOfIsland(self, grid):
    r, c = len(grid), len(grid[0])
    max_area = 0

    def dfs(row, col):
      # Base case: boundaries or water
      if row < 0 or row >= r or col < 0 or col >= c or grid[row][col] == 0:
        return 0


      grid[row][col] = 0


      return (
          1
          + dfs(row + 1, col)
          + dfs(row - 1, col)
          + dfs(row, col + 1)
          + dfs(row, col - 1)
      )

    for i in range(r):
      for j in range(c):
        if grid[i][j] == 1:
          max_area = max(max_area, dfs(i, j))

    return max_area

        