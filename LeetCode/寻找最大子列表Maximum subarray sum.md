#### 做算法题的三大步骤
    1.看懂题目的意思，明确要达到的效果
    2.构思解决的思路，不用考虑代码怎样写
    3.将思路转化为代码
- 基本实现了，使用的是穷举。但是时间复杂度爆表，为O(n*n)
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
- 让我看看别人怎么写的,逻辑更加的简洁，没有那么多限制条件
```

def maxSequence1(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0     # 这条语句很关键，curr为负数，就重新赋值为0，这会保证前面的值不会对后面产生影响
        if curr>max:max=curr
    return max
```
