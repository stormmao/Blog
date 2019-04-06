- 将长度超过 3 的单词除首尾字母外进行缩写，使用`re`库，用正则表达式取出所有长度大于4的字母，对这些字母进行相应的处理。[re正则表达式](http://www.runoob.com/python3/python3-reg-expressions.html)
```
import re

def abbreviate(s):
    list_of_words = re.findall(r'[A-Za-z]{4,}', s)

    for word in list_of_words:
        a10n_word = word[0] + str(len(word) - 2) + word[-1]
        s = s.replace(word, a10n_word)
    return s
```
- 简洁
```
import re

def abbreviate(s):
    repl = lambda w: w[0] + str(len(w) - 2) + w[-1]
    return re.sub('[a-zA-Z]{4,}', lambda m: repl(m.group(0)), s)
    ```
