# 第 k 大元素
> 先看看堆的定义：
堆是一种特殊的数据结构，它的通常的表示是它的根结点的值最大或者是最小。
python中heapq的使用
列出一些常见的用法：heap = []#建立一个常见的堆
heappush(heap,item)#往堆中插入一条新的值
item = heappop(heap)#弹出最小的值
item = heap[0]#查看堆中最小的值，不弹出
heapify(x)#以线性时间将一个列表转为堆
item = heapreplace(heap,item)#弹出一个最小的值，然后将item插入到堆当中。堆的整体的结构不会发生改变。
heappoppush()#弹出最小的值，并且将新的值插入其中
merge()#将多个堆进行合并
nlargest(n , iterbale, key=None)从堆中找出做大的N个数，key的作用和sorted( )方法里面的key类似，用列表元素的某个属性和函数作为关键字
  
这个题目使用小顶堆来实现，效率是最高的，只需要维护一个小顶堆就可以了，不会做是吃了没文化的亏。
```
class KthLargest(object):

    
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:     # 维护队堆的大小为 k 
            heapq.heappop(self.pool)  # 多于的数扔出去 

            
    def add(self, val):
        if len(self.pool) < self.k:   # 必须考虑的情景，堆的大小小于 k 
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:      # 大于堆顶元素就取而代之
            heapq.heapreplace(self.pool, val)
        return self.pool[0]           # 否则，直接返回堆顶元素
     
```
