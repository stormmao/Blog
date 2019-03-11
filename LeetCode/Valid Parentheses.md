# 判断括号是否对称
- Given a string containing just the characters '(', ')', '{', '}', '[' ,']', determine if the input string is valid.
 An input string is valid if:  
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.  
Note that an empty string is also considered valid.
```
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {"]":"[",")":"(","}":"{"} #字典的定义差点忘了格式，还有这里的 key-value 的括号是反着的，这样更加容易匹配
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():# 这里的判断条件刚开始写错了
                    return False
            else:
                return False
        return stack == [] # 栈清空了，就说明括号是左右对称的，返回 True
    
```
