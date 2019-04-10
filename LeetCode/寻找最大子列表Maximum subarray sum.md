#### 做算法题的三大步骤
    1.看懂题目的意思，明确要达到的效果
    2.构思解决的思路，不用考虑代码怎样写
    3.将思路转化为代码
```
def maxSequence(arr):
    maxnum = 0
    sum = 0
    while arr:
        for i in arr:
            sum += i
            if sum > maxnum:
                maxnum = sum
        arr = arr[1:]
        sum = 0
    return maxnum
```
