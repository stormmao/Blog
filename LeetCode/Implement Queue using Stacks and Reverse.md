# 使用栈实现队列的效果
- 这种实现的方式的重点是增加了 move 函数，使得整个函数的变得非常简洁，需要将 inStack 里的数搬移进 outStack 调用 move 函数就可以了。注意返回操作，返回正确的形式。
```
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack, self.outStack = [], []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.outStack.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.outStack[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return  (not self.outStack) and (not self.inStack)
    def move(self):   
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
                


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```
# 使用队列实现栈的效果
```
from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        q = self.queue
        q.append(x)
        for _ in range(len(q)-1):   #真是大坑，调试了才弄明白，len(q)-1为1，那么只会循环一次，以前以为会有0,1两次，为什么会这样想，是不是go的性质啊
            q.append(q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self.queue)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(8)
obj.push(9)
obj.push(10)
param_3 = obj.top()
param_2 = obj.pop()
param_4 = obj.empty()
print(param_2)
for i in range(1):     
    print(i)
```
