- 将连续出现的字符或数字聚集为一个，感觉很简单，但是不知道怎么下手，想到了集合去重，但是所有相同的元素都被去掉了,而且集合的顺序是无序的。看了一下
实现方法，很简单的。针对每一个元素，判断其与前一个是否一样，不一样就加入列表。
```
def unique_in_order(iterable):
    list = []
    flag = None
    for i in iterable:
        if i != flag:
            list.append(i)
            flag = i
    return list
```
- 使用库来实现,[groupby](https://docs.python.org/zh-cn/3/library/itertools.html?highlight=groupby#itertools.groupby)
```
from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]
```
