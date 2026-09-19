class Solution(object):
    def pacificAtlantic(self, heights):
        pacific = set()
        atlantic = set()
        row = len(heights)
        col = len(heights[0])

        def dfs(prev_height, r, c, seen):
            if r < 0 or r >= row or c < 0 or c >= col:
                return
            
            if (r, c) in seen or prev_height > heights[r] [c]:
                return
            seen.add((r, c))  

            h = heights[r][c] 
            dfs(h, r-1, c, seen)
            dfs(h, r+1, c, seen)
            dfs(h, r, c+1, seen)
            dfs(h, r, c-1, seen)

        #top and bottom
        for i in range(0, col):
            dfs(-1, 0, i, pacific)
            dfs(-1, row - 1, i, atlantic)

        #left and right
        for i in range(0, row):
            dfs(-1, i, 0, pacific)
            dfs(-1, i, col-1, atlantic)

        res = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    res.append([i,j])

        return res