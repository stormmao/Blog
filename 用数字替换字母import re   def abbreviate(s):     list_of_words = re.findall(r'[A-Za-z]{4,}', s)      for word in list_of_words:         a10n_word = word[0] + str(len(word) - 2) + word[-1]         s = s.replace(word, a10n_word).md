- 替换多个分隔符
```
import re

def abbreviate(s):
    list_of_words = re.findall(r'[A-Za-z]{4,}', s)

    for word in list_of_words:
        a10n_word = word[0] + str(len(word) - 2) + word[-1]
        s = s.replace(word, a10n_word)
```
