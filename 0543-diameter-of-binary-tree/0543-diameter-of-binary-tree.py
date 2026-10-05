class Solution(object):
    def diameterOfBinaryTree(self, root):
        # Keep a tracker for the max diameter found so far
        self.res = 0

        def dfs(node):

            if node == None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            diameter = left + right

            self.res = max(self.res, diameter)

            height = max(left, right) + 1

            return height

        dfs(root)    
        return self.res        