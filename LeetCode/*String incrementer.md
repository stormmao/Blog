## 字符串自增
- 自己写的代码自能通过初步测试，最终测试过不了，原因出在如果字符串中间存在数字的话，结果会出错，因为我使用的使遍历字符串，并提取出所有的数字。虽然没有
成功，但是还是有一些收获。首先是知道了怎么把字符串每个元素分隔开。使用列表化语句`ls = list(strng)`。还有简写字符串判断语句：
```
for i in ls:
    if i.isdigit():
        srr += i
等价于
srr = ''.join(s for s in ll if s.isdigit())
```
- 最终我写出的代码如下，反思了一下，我的时间复杂度很高。考虑了一下新的实现方法，反向遍历。
```
def increment_string(strng):
    ls = list(strng)
    newstr = ''
    num = 0
    count = 0
    if not strng:
        return '1'
    for i in ls:
        if i.isdigit():
            newstr += i
    if len(newstr) == 0:
        return strng + '1'
    count = len(newstr)
    num = int(newstr) + 1
    return strng[:-count]+'0'*(count - len(str(num)))+str(num)
```
- 在思考反向遍历的时候，找到了怎样反转字符串`newstr = newstr[::-1]`，没想到居然成功了，过程很辛苦。不过基本实现了，时间复杂度也降低了，就是代码
比较冗余，下一步简化代码。
```
def increment_string(strng):
    ls = list(strng)
    ls.reverse()     ### 反转列表
    newstr = ''
    num = 0
    count = 0
    if not strng:
        return '1'
    for i in ls:
        if i.isdigit():
            newstr += i
        else:
            break
    if len(newstr) == 0:
        return strng + '1'
    newstr = newstr[::-1] ### 反转字符串
    count = len(newstr)
    num = int(newstr) + 1
    # count = count - len(str(num))
    return strng[:-count]+'0'*(count - len(str(num)))+str(num)
print(increment_string('oo05p1'))
```
- 哎呦喂，别人的代码很简单啊~rstrip() **删除 string 字符串末尾的指定字符（默认为空格）**,zfill (width)返回长度为 width 的字符串，原字符串右对齐，
前面填充0
```
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
```
- 使用正则表达式实现
```
import re

def increment_string(input):
    match = re.search("(\d*)$", input)
    if match:
        number = match.group(0)
        if number is not "":
            return input[:-len(number)] + str(int(number) + 1).zfill(len(number))
    return input + "1"
```
