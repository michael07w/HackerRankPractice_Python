# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse(head):
    """Reverses a singly linked list.
    Solution to Hackerrank challenge: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

    Args:
        head (SinglyLinkedListNode): The head of the linked list

    Returns:
        head (SinglyLinkedListNode): The new head of the linked list, after reversal
    """
    # return null linked list
    if head == None:
        return head

    current_node = head
    prev_node = next_node = None

    while current_node != None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    # prev_node now points to new head
    return prev_node
