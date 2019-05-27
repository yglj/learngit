class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


def addTwoNumbers(self,l1,l2):
    p = result =  ListNode(-1)
    carry = 0
    while l1 and l2:
        p.next = ListNode(l1.val + l2.val +carry)
        carry = p.next.val // 10
        p.next.val %= 10
        p = p.next
        l1 = l1.next
        l2 = l2.next
    remain = l1 or l2
    while remain:
        remain.next = ListNode(remain.val)
    return result.next
print(addTwoNumbers())