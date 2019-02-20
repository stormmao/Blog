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

class Solution():
    def mergeTwoLists(self, l1, l2):
        node = dummy = ListNode(-1)#此处是新建链表，0是其初始元素，可以随便定义，dummy是一个哨兵，方便返回整个链表
        while l1 and l2:
            if l1.val >= l2.val: #这里最好画图理解一下，是一步步把较小的数据调上来，到最后指向空，会把l2剩下的所有数据调换过来
                l1, l2 = l2, l1
            node.next = l1
            l1 = l1.next 
            node = node.next
        node.next = l1 or l2#如果其中一个链表为空，就会执行这条语句，返回不为空的链表
        return dummy.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        node, dummy = ListNode(0) #这里赋值发生错误，害我找了好久
        while l1 and l2:
            if l1.val >= l2.val:
                l1, l2 = l2, l1                
            node.next = l1
            l1 = l1.next 
            node = node.next
        node.next = l1 or l2 
        return dummy.next
```
## 迭代法
```
def mergeTwoLists(self, l1, l2):
    node = dummy = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            node.next = ListNode(l1.val)  # or l1
            l1 = l1.next
        else:
            node.next = ListNode(l2.val)  # or l2
            l2 = l2.next
        node = head.next
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
## 完整版实现
-  由于不能理解链表元素怎样依照大小提取出来，所以进行了调试，找到了原因。l1, l2 = l2, l1 因为这一步是交换指针的地址，不是仅仅交换数值，指针在俩个链表之间来回移动，选取较小的值插入新的链表
```
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution():
    def mergeTwoLists(self, l1, l2):
        node = dummy = ListNode(-1)#此处是新建链表，0是其初始元素，可以随便定义，dummy是一个哨兵，方便返回整个链表
        while l1 and l2:
            if l1.val >= l2.val:
                l1, l2 = l2, l1
            node.next = l1
            l1 = l1.next
            node = node.next
        node.next = l1 or l2#如果其中一个链表为空，就会执行这条语句，返回不为空的链表
        return dummy.next

if __name__=='__main__': #创建l1和l2两个链表，注意，排序好的就需要arr1和arr2中数字从小到大
    arr1 = [0,2,5]
    arr2 = [1,3,4]
    l1 = ListNode(arr1[0])
    p1 = l1
    l2 = ListNode(arr2[0])
    p2 = l2
    for i in arr1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for i in arr2[1:]:
        p2.next = ListNode(i)
        p2 = p2.next
    s=Solution()#新建一个类才能调用其中的方法
    q=s.mergeTwoLists(l1,l2)
    while q:
        print(q.val)
        q = q.next

```
