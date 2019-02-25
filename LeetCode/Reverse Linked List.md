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
        p, pr = head, None
        while p:
            pn = p.next #pr指针保留前面的节点，pn指针保留后面的节点，p指针就这样一步步遍历反转整个链表
            p.next = pr  #指针的操作过程中，都是先保存后指向地址，再改变指针指向，要不然会造成地址丢失
            pr = p       #这三行代码作可以合成一行：pn, p.next, pr = p.next, pr, p
            p = pn
        return pr        #最后p,pn都会指向None
```
