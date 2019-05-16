class Node:
    def __init__(self, val, _next=None):
        self.val = val
        self.next = _next


def reverse_print_linked_list(root):
    """反向打印单链表，第一反应就是将每个值拿出来放到列表中，然后从后往前打印
    其实这个列表就起到栈的作用，所以我觉得就是很多概念虽然用到了，但是没有抽象化，应该注意一下这点"""
    cur = root
    values = []
    while cur:
        values.append(cur.val)
        cur = cur.next
    for val in values[::-1]:
        print(val)


def recursion_reverse_print_linked_list(root):
    """既然可以用栈，那摆明就可以用递归嘛"""
    if root is None:
        return
    recursion_reverse_print_linked_list(root.next)
    print(root.val)


if __name__ == "__main__":
    node_1 = Node(2)
    node_2 = Node(5)
    node_3 = Node(9)
    node_4 = Node(1)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    linked_list = node_1

    reverse_print_linked_list(linked_list)
    recursion_reverse_print_linked_list(linked_list)
