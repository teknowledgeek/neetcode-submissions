class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        coinDP = [0]*n
        
        for i in range(1,len(coinDP)):
            countCoin = []
            for c in coins:
                # if i < c:
                    # countCoin.append(-1) 
                if i >= c:
                    count =  1 + coinDP[i-c] if coinDP[i-c] >= 0 else -1
                    if count > 0:
                        countCoin.append(count) 
            coinDP[i] = min(countCoin) if countCoin else -1
            # print(i, c, countCoin, coinDP)
        return coinDP[amount]