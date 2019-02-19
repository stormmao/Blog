# 检测链表中的环
- 使用快慢指针，当慢指针追上快指针，则证明有环的存在
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pr, pn = head, head
        if not head:
          return False
        while pn and pn.next:#此处只能用快指针作为判定条件，快指针跑得更快，当其到达链表尾部时，整个循环停止，要不然慢指针就追上来了
          pr = pr.next
          pn = pn.next.next
          if pr == pn:
            return True
        else:
          return False
  ```
