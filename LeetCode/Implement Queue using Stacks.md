# 使用栈实现队列的效果
- 这种实现的方式的重点是增加了 move 函数，使得整个函数的变得非常简洁，需要将 inStack 里的数搬移进 outStack 调用 move 函数就可以了。注意返回操作，返回正确的形式。
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
