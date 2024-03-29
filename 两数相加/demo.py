"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = 0
        st = ListNode(0)
        start = st
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            tp = (x + y + add) % 10
            add = (x + y + add) // 10
            start.next = ListNode(tp)
            start = start.next
            if l1 != None: 
                l1 = l1.next
            if l2 != None: 
                l2 = l2.next
        if add > 0:
            start.next = ListNode(1)
        return st.next
