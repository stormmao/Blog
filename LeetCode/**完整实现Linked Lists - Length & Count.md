## 计算链表的长度和相应元素的个数
- 这题本来是很简单的，但是我忘了链表的相关使用方法了，老是出错，对链表指针和指向值没有搞清楚，查阅了很多资料，才算初步弄清楚了。这个久了没看
就生疏了，看自己以前的代码，都有点迷糊了，趁这个机会再好好理理。
    - 这里有几点要注意，函数声明在类里面和外面使用起来是完全不一样的，这里只声明了节点类，没有想应的方法，需要自己初始化的时候实现； 
    - 这里 __init__ 方法里的 data 和 count 函数里的 data 是不一样的，不要搞混了，所以参数还是尽量设置不一样的名字；
    - current 是 Node 类型的，要访问的时候要加上初始化中的方法 self.data，我在比较值的时候就忘了加，导致出错；
    - 类的实现可以有好几种方式，[这里的例子可以好好参考一下](https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/)
```
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def count(node, data):
    current = node
    countdata = 0
    print(type(current))
    while current is not None:
        if current.data == data: # 刚开始写成 if current == data 结果报错了
            countdata += 1
        current = current.next
    return countdata

def length(node):
    current = node
    countlen = 0
    if current is None:
        return
    while current is not None:
        countlen += 1
        current = current.next
    return countlen

def main():
    node = Node(1)  # 给链表存入数据
    p1 = Node(2)  # 建立链表1->2->3->4->None;
    p2 = Node(3)
    p3 = Node(4)
    node.next = p1
    p1.next = p2
    p2.next = p3
    ps = count(node,9)
    pp = length(node) # 输出链表 4->3->2->1->None
    print(pp,ps)

if __name__ == '__main__':

```
- 参考别人的代码，发现我有些代码是多余的`current = node`可以直接使用`node`
```
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng
  
def count(node, data):
    c = 0
    while node:
        if node.data==data:
            c += 1
        node = node.next
    return c
```

