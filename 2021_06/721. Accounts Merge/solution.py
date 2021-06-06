from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_account = defaultdict(list)
        result = []
        visited = set()
        
        for idx, account in enumerate(accounts):
            # name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_account[email].append(idx)
        
        def dfs(idx, emails):
            if idx in visited:
                return
            visited.add(idx)
            for e in accounts[idx][1:]:
                emails.add(e)
                for j in email_to_account[e]:
                    dfs(j, emails)

        for idx, account in enumerate(accounts):
            name, emails = account[0], set()
            if not idx in visited:
                dfs(idx, emails)
                result.append([name] + sorted(emails))
            
        return result
