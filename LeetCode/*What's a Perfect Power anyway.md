- In mathematics, a perfect power is a positive integer that can be expressed as an integer power of another positive integer.
More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
- 判断一个数是不是完美数，有没有一个数的多次方能够等于这个数
```
from math import log, sqrt
def isPP2(n):
    m=int(sqrt(n))
    for i in range(2,m+1):
        k=0
        while i**k < n:
            k+=1
        if i**k==n:
            return [i,k]
```
- 高极写法[round函数](https://docs.python.org/zh-cn/3/library/functions.html?highlight=round#round)
```
from math import ceil, log, sqrt

def isPP(n):
    for b in xrange(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None
```
