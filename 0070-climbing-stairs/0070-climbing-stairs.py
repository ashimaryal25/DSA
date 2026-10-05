class Solution(object):
    def climbStairs(self, n):

        if n == 1:
            return 1

        if n == 2:
            return 2
                
        one_step_back = 2
        two_step_back = 1

        cur = 0
        for n in range(3, n+1):
            temp = one_step_back
            cur = one_step_back + two_step_back
            one_step_back = cur
            two_step_back = temp


        return cur    



        
        