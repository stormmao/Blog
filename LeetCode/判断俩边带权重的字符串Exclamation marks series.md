# [题目详情](https://www.codewars.com/kata/exclamation-marks-series-number-17-put-the-exclamation-marks-and-question-marks-to-the-balance-are-they-balanced/python)
- 看到这道题，第一时间想到了使用`counter`来计算每个字符出现的次数，再乘以权重进行比较。
```
from collections import Counter  
def balance(left, right):
    countl = Counter(left)
    countr = Counter(right)
    if countl['!']*2+countl['?']*3 > countr['!']*2+countr['?']*3: # 像这种判断语句，应该把最大概率出现的情况放在最前面，最小概率的放在
    最后面，可以提高运行的效率。
        return "Left"
    elif countl['!']*2+countl['?']*3 < countr['!']*2+countr['?']*3:
        return "Right"
    else:return "Balance"
```
- 忽然想起，字符串自带计算个数的函数[counter](http://www.runoob.com/python3/python3-string-count.html)
```
def balance(left, right):
    val = ((left.count('!') * 2) + (left.count('?') * 3)) - ((right.count('!') * 2) + (right.count('?') * 3))
    return 'Right' if val < 0 else 'Left' if val > 0 else 'Balance'
```
