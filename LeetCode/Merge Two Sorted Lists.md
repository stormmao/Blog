# 合并两个有序链表
- Merge two sorted linked lists and return it as a new list. The new list should be made by 
  splicing together the nodes of the first two lists.
- 分析：中规中矩的做法是新建一个链表，比较两个有序链表的大小，依次插入新链表；比较炫酷的做法是使用递归和迭代，有点烧老壳
## 普通做法
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        node, dummy = ListNode(0) #此处是新建链表，0是其初始元素，可以随便定义，dummy是一个哨兵，方便返回整个链表
        while l1 and l2:
            if l1.val >= l2.val:z #这里最好画图理解一下，是一步步把较小的数据调上来，到最后指向空，会把l2剩下的所有数据调换过来
                l1, l2 = l2, l1                
            node.next = l1
            l1 = l1.next 
            node = node.next
        node.next = l1 or l2
        return dummy.next
```
## 递归法
```
class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
         if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2) #原理是一样的，不过理解起来还是很烧脑的，画画图方便理解
         return l1 or l2
```
