# 输出链表的后半段
- 要求： Given a non-empty, singly linked list with head node head, return a middle node of linked list.If there are two middle nodes, 
return the second middle node
- 分析：通过画图得知，当设置快慢指针时，当快指针到达链表尾部，慢指针停止的位置正好满足条件，前提是快指针速度是慢指针的两倍
- 哈哈，居然做出来了，不过有点小问题，return语句应该放在while语句的外面，要不然返回的指针是错误的，刚开始跑一步勒！
- 代码：
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        slow, fast = head, head
        while not head :
            return False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
```
