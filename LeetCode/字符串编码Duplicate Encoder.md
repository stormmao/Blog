- 针对一串输入的字符串，如果存在重复的（无论大小写）就返回')',不重复就返回'('。
- 本来是很简单的，但是感觉现在对好多库函数不了解，没有第一时间想到使用库函数，而是使用原始的遍历，但是遍历的结果不理想，重复判断了。
```
from collections import Counter
def duplicate_encode(word):
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for x in word:
        if count[x] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string
```
- 简洁明了
> Counter({'p': 2, 'i': 2, 'o': 1, 'k': 1, 'a': 1})函数会统计字符串的每个字母的个数，并返回一个字典类型。
```
from collections import Counter
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
```
