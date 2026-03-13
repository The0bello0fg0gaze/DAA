class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n + 1):
                x = s[start:end]
                if x == x[::-1]:
                    for each in dp[end]:
                        new = [x]
                        new.extend(each)
                        dp[start].append(new)
        print(dp)
        return dp[0]

