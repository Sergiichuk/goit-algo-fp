class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head

        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node

        self.head = sorted_list

    def _sorted_insert(self, head, node):
        if head is None or node.data < head.data:
            node.next = head
            return node

        current = head
        while current.next and current.next.data < node.data:
            current = current.next

        node.next = current.next
        current.next = node
        return head


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.data < p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    if p1:
        tail.next = p1
    if p2:
        tail.next = p2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list



list1 = LinkedList()
list1.append(3)
list1.append(1)
list1.append(5)

list2 = LinkedList()
list2.append(4)
list2.append(2)
list2.append(6)

print("Початковий список 1:")
list1.print_list()

print("Реверс списку 1:")
list1.reverse()
list1.print_list()

print("Сортування списку 1:")
list1.insertion_sort()
list1.print_list()

print("Сортування списку 2:")
list2.insertion_sort()
list2.print_list()

print("Об'єднання двох відсортованих списків:")
merged = merge_sorted_lists(list1, list2)
merged.print_list()
