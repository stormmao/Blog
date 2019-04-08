- 这道题简直是一脸懵逼，感觉很简单，但是不知道怎么去实现。感觉递归类型的题目有时候真的很难理清楚思路啊，或许应该画画图，做一下程序设计。
- [实现过程的详细解释](https://stackoverflow.com/questions/28713934/how-to-implement-unary-function-chainer-using-python)
```
def chained(functions):
    def f(x):
        for function in functions:
            x = function(x)
        return x
    return f
```
- [’reduce‘ 函数](http://www.runoob.com/python/python-func-reduce.html)
```
def chained(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)
```
