class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [[0 for _ in range(target + 1)] for _ in range(len(prob) + 1)]
        dp[0][0] = 1
        for idx in range(1, len(prob) + 1):
            dp[idx][0] = dp[idx - 1][0] * (1 - prob[idx - 1])
        for idx in range(1, len(prob) + 1):
            for k in range(1, target + 1):
                dp[idx][k] = (
                    dp[idx - 1][k] * (1 - prob[idx - 1]) +
                    dp[idx - 1][k - 1] * prob[idx - 1]
                )

        return dp[-1][-1]

    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        prev = [0 for _ in range(target + 1)]
        prev[0] = 1
        for idx in range(len(prob)):
            curr = [0 for _ in range(target + 1)]
            curr[0] = prev[0] * (1 - prob[idx])
            for k in range(1, target + 1):
                curr[k] = prev[k - 1] * prob[idx] + prev[k] * (1 - prob[idx])
            prev = curr
        return prev[-1]

