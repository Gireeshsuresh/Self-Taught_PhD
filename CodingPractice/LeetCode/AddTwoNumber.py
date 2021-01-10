from typing import List

class ListNode:
    def __init__(self, val=0 , next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode()
        cur_ptr = result
        carry = 0

        while l1 or l2 or carry:
            # Get the Values from the Linked List. If no value return 0.
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            # Get the value of result (sum of val_1 and val_2)
            temp = val_1 + val_2 + carry
            carry = temp // 10
            temp = temp % 10
            cur_ptr.next = ListNode(temp)

            # Update Pointer location
            cur_ptr = cur_ptr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

def list2link(l):
    if len(l) == 0:
        return None
    ret_tail = ret_head = ListNode(l[0])
    for val in l[1:]:
        tmp = ListNode(val)
        ret_tail.next = tmp
        ret_tail = ret_tail.next
    return ret_head


def print_link(link):
    while link is not None:
        print("{}" .format(link.val), end='')
        if link.next:
            print(" -> ", end='')
        link = link.next
    print("\n")



if __name__ == "__main__":
    mySolution = Solution()
    
    a = list2link([2,4,3])
    b = list2link([5,6,4])
    
    print("Input L1  :")
    print_link(a)
    print("Input L2  :")
    print_link(b)

    result = mySolution.addTwoNumbers(a,b)
   
    print("Output : ")
    print_link(result)