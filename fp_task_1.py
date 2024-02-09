class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Функція для реверсування однозв'язного списку


def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Алгоритм сортування вставками для однозв'язного списку


def insertion_sort(head):
    if head is None or head.next is None:
        return head

    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = insert_node(sorted_head, current)
        current = next_node

    return sorted_head


def insert_node(sorted_head, new_node):
    if sorted_head is None or sorted_head.data >= new_node.data:
        new_node.next = sorted_head
        return new_node

    current = sorted_head
    while current.next and current.next.data < new_node.data:
        current = current.next
    new_node.next = current.next
    current.next = new_node
    return sorted_head

# Функція, яка об'єднує два відсортовані однозв'язні списки в один відсортований список


def merge_sorted_lists(head1, head2):
    dummy_node = Node(None)
    current = dummy_node

    while head1 and head2:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    # Сортування об'єднаного списку
    dummy_node.next = insertion_sort(dummy_node.next)

    return dummy_node.next


# Приклади використання функцій
if __name__ == "__main__":
    # Створення першого списку: 1 -> 3 -> 5 -> 7 -> 9
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head1.next.next.next = Node(7)
    head1.next.next.next.next = Node(9)

    # Створення другого списку: 2 -> 10 -> 3 -> 23 -> 11
    head2 = Node(2)
    head2.next = Node(10)
    head2.next.next = Node(3)
    head2.next.next.next = Node(23)
    head2.next.next.next.next = Node(11)

    print("Перший список:")
    print_list(head1)

    print("Другий список:")
    print_list(head2)

    # Реверсування першого списку
    head1 = reverse_linked_list(head1)
    print("Реверс першого списку:")
    print_list(head1)

    # Сортування другого списку
    head2 = insertion_sort(head2)
    print("Відсортований другий список:")
    print_list(head2)

    # Об'єднання двох відсортованих списків
    merged_head = merge_sorted_lists(head1, head2)
    print("Об'єднаний відсортований список:")
    print_list(merged_head)
