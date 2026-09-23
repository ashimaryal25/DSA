import heapq
from collections import defaultdict

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        heapq.heapify(hand)

        nums = defaultdict(int)

        for h in hand:
            nums[h] += 1

        while hand:
            cur = hand[0]

            for i in range(groupSize):
                needed = cur + i

                if nums[needed] == 0:
                    return False

                nums[needed] -= 1

            while hand and nums[hand[0]] == 0:
                heapq.heappop(hand)

        return True
                    

        if len(hands) == 0:
            return ans
        else:
            return false    

            
        