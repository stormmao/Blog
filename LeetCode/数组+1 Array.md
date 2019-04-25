- 这道题其实比较简单，刚开始想通过投机取巧的方法做出来，但是会涉及到一些情况处理不了的时候，下面的代码就是例子。
```
def up_array(arr):
    for i in arr:
        if i < 0:
            return None
    if arr[-1] == 9:
        arr[-2]+=1
        arr[-1]=0
        return arr
    else:
        arr[-1]+=1
        return arr
```
- 综合考虑了条件，重新写代码，虽然步骤有点繁琐，但是所有情况都考虑进去了。
```
def up_array1(arr):
    strn = ''
    lnum = []
    for i in arr:
        if i < 0 or i > 9:
            return None
        else:
            strn += str(i)
    num = int(strn) + 1
    for i in str(num):
        lnum.append(int(i))
    return lnum
```
- 不够简洁，看了一下别人的条件判断语句，集成度更高，更容易读。
```
def up_array(arr):
  if not arr or min(arr) < 0 or max(arr) > 9:
    return None
  else:
    return [int(y) for y in str(int("".join([str(x) for x in arr])) + 1)]# 看清楚括号的范围，实现的思路和我的是一样的
```
