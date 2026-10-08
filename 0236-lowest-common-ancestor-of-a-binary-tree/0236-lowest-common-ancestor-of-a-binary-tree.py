class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root   

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right        

        
        


           






        