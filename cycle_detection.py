# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    slow_ptr = fast_ptr = head

    while (fast_ptr != None and fast_ptr.next != None):
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if fast_ptr == slow_ptr:
            return True

    return False
