# 反转链表
- 使用三指针可以实现高效反转
```
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p, q = head, None
        while p:
            pr = p.next #q指针保留前面的节点，pr指针保留后面的节点，p指针就这样一步步遍历反转整个链表
            p.next = q  #指针的操作过程中，都是先保存后指向地址，再改变指针指向，要不然会造成地址丢失
            q = p       #这三行代码作可以合成一行：pr, p.next, q = p.next, q, p
            p = pr
        return q
```
