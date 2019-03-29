- You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest 
number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
- Example
> Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
- You may assume that you have an infinite number of each kind of coin.
- 理一下自己的思路，考虑对输入的列表进行排序。因为是贪婪算法，所以使用从大到小排序`lp=sorted(coin,reverse=True)`。然后遍历整个排序的列表，从大到小
每次都使用`amount -= lp[i] for i in range(len(lp)) if amount > lp[i]:`对 amount 进行处理，但是这种算法有一个很大弊端，不能够罗列出所有的情况
。举一个例子`[1,2,5],11`是可以由`5，5，1`满足条件。但是如果是`[2,3,6],13`z这种解法会先使用2个6，然后会发现无解，但其实`6,3,2,2`就是解。
- 利用 BFS 的思想来解决这道题。
```
def coinChange(coins, amount):
    level = seen = {0}
    number = 0
    while level:
        if amount in level:
            return number
        level = {a+c for a in level for c in coins if a+c <= amount} - seen # 差集
        seen |= level                                                       # 并集
        number += 1
    return -1
```
- xrange() 函数用法与 range 完全相同，所不同的是生成的不是一个数组，而是一个生成器。
> Assume dp[i] is the fewest number of coins making up amount i, then for every coin in coins, dp[i] = min(dp[i - coin] + 1).
The time complexity is O(amount * coins.length) and the space complexity is O(amount)  
```
class Solution(object):
    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in xrange(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == MAX]
```
```
[dp[amount], -1][dp[amount] == max_val] => [dp[amount], -1][0 or 1]
if dp[amount] == max_val: [dp[amount], -1][1] => -1
else: [dp[amount], -1][0] => dp[amount]
 it'd be a little bit more readable regarding the line return [dp[amount], -1][dp[amount] == MAX], 
 it could be shorter as return [dp[-1], -1][dp[-1] == MAX], where dp[-1] is the right most element of dp.
```
