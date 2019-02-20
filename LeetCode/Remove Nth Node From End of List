# 删除倒数第N个链表数据，并且输出新的链表
- Given a linked list, remove the n-th node from the end of list and return its head.
- 写这个代码的时候到处都是错，都要调试疯了，多看看，看清楚每个语句的关键词
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        p = q = head #刚开始我还加了一个哨兵，结果发现没有必要
        for _ in range(n): #这个语句我换了好几种写法
            p = p.next
        if not p:
            return head.next #这里是针对一个元素的链表
        while p.next:  #这里刚开始用的if语句，天啦！错得离谱，还有这里是p.next不是p
            p = p.next
            q = q.next
        q.next = q.next.next
        return head
```
