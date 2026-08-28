class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        def dfs(node, p, q):
            if not node:
                return None

            if node == p or node == q:
                return node   

            left =  dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left  and right:
                return node

            # Then check individually
            if left is not None:
                return left

            if right:
                return right

            return None



        return dfs( root, p, q )    






        