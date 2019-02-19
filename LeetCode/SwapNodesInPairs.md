# 反转链表中的相邻元素
- 示例：Given 1->2->3->4, you should return the list as 2->1->4->3
- 实现代码：  
/* Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None */

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pr, pr.next = self, head
        while pr.next and pr.next.next:
          a = pr.next
          b = a.next
          pr.next, b.next, a.next = b, a, b.next#pr.next = b 的作用是衔接翻转后的节点
          pr = a
        return self.next 
