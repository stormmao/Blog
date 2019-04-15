- 这道题糟糕透了，输出的排序完全是错的，鬼知道他是怎么排的序，反正基本的功能是实现了，就是最后的按要求输出字符串不行，老是报错，
观察报错的原因，以为要按字母大小排序，结果不行。按照输入的顺序排序，也不行，它的顺序乱排的吧，无语了！
```
def stock_list(listOfArt, listOfCat):

    dictbook = dict.fromkeys(listOfCat,0)
    ls = ''
    for ch in listOfCat:
        for char in listOfArt:
            if ch == char[0] :
                dictbook[ch] += int(char.split(' ')[1])
    for i in dictbook.keys():
        ls += '(' + i + ' : ' + str(dictbook[i]) + ') - '
    return ls[:-3]

a = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
b = ["A", "C","B","D"]
print(stock_list(a, b))
```
- 这种写法里面有我想学习的东西，格式控制输出
- Counter类的目的是用来&跟踪值出现的次数&。它是一个无序的容器类型，以字典的键值对形式存储，其中元素作为key，
其计数作为value。计数值可以是任意的Interger（包括0和负数）。 Counter 类有点像其他语言中的 bags或multisets
```
from collections import Counter

def stock_list(listOfArt, listOfCat):
    if not listOfArt:
        return ''
    codePos = listOfArt[0].index(' ') + 1# 返回 ’ ‘ 处的索引
    cnt = Counter()    # 非常关键的语句
    for s in listOfArt:
        cnt[s[0]] += int(s[codePos:])
    return ' - '.join('({} : {})'.format(cat, cnt[cat]) for cat in listOfCat)## 这就是我刚开始想写的，不用遍历字典
    ## for cat in listOfCat 使时间复杂度大大降低，不用遍历给出的目录了。
```
