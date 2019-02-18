class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):  # 循环的方法反转链表
    if head is None or head.next is None:
        return head
    p = head
    q = None
    while p:
        pr = p.next
        p.next = q
        q = p
        p = pr
    return q


head = ListNode(1)  # 测试代码
p1 = ListNode(2) # 建立链表1->2->3->4->None;
p2 = ListNode(3)
p3 = ListNode(4)
head.next = p1
p1.next = p2
p2.next = p3
pp = reverseList(head)  # 输出链表 4->3->2->1->None
while pp:
    print(pp.val)
    pp = pp.next
