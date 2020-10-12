# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        count_zero_1 = 0
        count_zero_2 = 0
        number_seen = False
        val1 = 0
        val2 = 0
        while (l1 != None):
            if l1.val == 0 and number_seen == False:
                count_zero_1 += 1
                l1 = l1.next
            else:
                number_seen = True
                if l1.val < 0 or l1.val > 9:
                    return None
                val1 = val1 * 10 + l1.val
                l1 = l1.next
                count += 1
                if count > 100:
                    return None
        number_seen = False

        count = 0
        while (l2 != None):
            if l2.val == 0 and number_seen == False:
                count_zero_2 += 1
                l2 = l2.next
            else:
                number_seen = True
                if l2.val < 0 or l2.val > 9:
                    return None
                val2 = val2 * 10 + l2.val
                l2 = l2.next
                count += 1
                if count > 100:
                    return None

        val1 = int(str(val1)[::-1])
        val2 = int(str(val2)[::-1])

        val1 = val1 * (10 ** count_zero_1)
        val2 = val2 * (10 ** count_zero_2)

        val = val1 + val2

        if val == 0:
            return ListNode(0, None)
        nodes = []
        while (val != 0):
            print(val)
            digit = val % 10
            val = val // 10
            temp = ListNode(digit, None)
            nodes.append(temp)

        first = nodes.pop(0)
        if len(nodes) == 0:
            return first
        if len(nodes) == 1:
            first.next = nodes.pop()
        i = 0
        while (i < (len(nodes) - 1)):
            if i == 0:
                first.next = nodes[i]
            nodes[i].next = nodes[i + 1]
            i += 1
        return first
