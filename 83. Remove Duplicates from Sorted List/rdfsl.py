#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteD(self, head):
        # st = {}
        # current = head
        # prev = None
        
        # while current:
        #     if str(current.val) in st:
        #         prev.next = current.next
        #     else:
        #         st[str(current.val)] = current.val
        #         prev = current
        #     current = current.next
        # return head
        
        current = head
        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
                continue
            
            current = current.next
        
        return head
        
s = Solution()
values = [1,1,1,2,3,4,4]

head = ListNode(values[0])
current_node = head

for value in values[1:]:
    current_node.next = ListNode(value)
    current_node = current_node.next


current_node = s.deleteD(head)
while current_node:
    print(current_node.val)
    current_node = current_node.next