- 反转输入的数字，主要考虑带负号还有反转之后是否会超出范围，整个实现过程比较简单。
    [题目链接](https://leetcode.com/problems/reverse-integer/description/)
```
def reverse(x: int) -> int:
    strx = str(x)
    newstr = ''
    if not strx[0].isdigit():
        newstr = strx[1:]
        newstr = newstr[::-1]
        if int(newstr) > 2**31:
            return 0
        return -int(newstr)
    else:
        if int(strx[::-1]) > 2**31-1:
            return 0
        return int(strx[::-1])
```
- 看起来逻辑更加清晰
```
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            y=str(abs(x))
            y=y[::-1]
            y='-'+y
            
        else:
            y=str(x)
            y=y[::-1]

        if int(y)<-2**31 or int(y)>2**31-1:
            return 0
        else:
            return (int(y))
```
