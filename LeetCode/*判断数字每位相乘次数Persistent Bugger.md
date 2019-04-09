- 没有想出来啊，坐在床上编程效率有点低啊，这道题其实是不难的，我已经想到使用迭代，字符串转化了，不过还没拼接起来。还有这里使用的是列表进行迭代，我想的
是用字符串进行迭代，但是会很麻烦。
    - [reduce函数](https://www.geeksforgeeks.org/reduce-in-python/)
    ###########
```
import functools
def persistence(n):
    nums = [int(x) for x in str(n)]
    count = 0
    while len(nums) > 1:
        newNum = functools.reduce(lambda x, y: x * y, nums)
        nums = [int(x) for x in str(newNum)]
        count = count + 1
    return count
```
- 使用另外一个库[’operator‘](https://docs.python.org/zh-cn/3/library/operator.html?highlight=operator)实现
```
import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
```
