from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        email_to_name = {}

        # build graph
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name

            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)

        visited = set()
        res = []

        def dfs(email, group):
            visited.add(email)
            group.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, group)

        # find connected components
        for email in email_to_name:
            if email not in visited:
                group = []

                dfs(email, group)

                name = email_to_name[email]
                res.append([name] + sorted(group))

        return res