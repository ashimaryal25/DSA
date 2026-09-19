class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        p = power
        score = 0
        length = len(tokens)

        q = deque(sorted(tokens))

        # if facedown at last dont play
        while q:
            
            if p >= q[0] :
                p -= q.popleft()
                score += 1
            else:
                if score == 0:
                    break

                if len(q) == 1:
                    break 

                score -= 1
                p += q.pop()
        return score



        