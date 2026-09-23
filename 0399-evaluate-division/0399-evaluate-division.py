from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        search = defaultdict(list)

        # build graph
        for i, (a, b) in enumerate(equations):
            search[a].append((b, values[i]))
            search[b].append((a, 1 / values[i]))

        def dfs(first, second, visited):
            # variable doesn't exist
            if first not in search or second not in search:
                return -1.0

            # found destination
            if first == second:
                return 1.0

            visited.add(first)

            # try every variable connected to first
            for cur_var, factor in search[first]:

                if cur_var not in visited:
                    result = dfs(cur_var, second, visited)

                    if result != -1:
                        return factor * result

            return -1.0

        res = []

        for a, b in queries:
            res.append(dfs(a, b, set()))

        return res
        
        