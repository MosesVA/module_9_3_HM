from double_linked_list import LinkedList, Node


class MyLinkedList(LinkedList):

    def insert_at_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        count = 0
        if index == 0:
            self.insert_at_head(data)
            return f"Добавление по индексу. Теперь в голове узел с данными {self.head.data}"
        elif index >= self.len_ll() - 1:
            self.insert_at_tail(data)
            return f"Добавление по индексу. Теперь в хвосте узел с данными {self.tail.data}"
        elif index < self.len_ll():
            while current_node:
                if count == index:
                    new_node.next_node = current_node
                    new_node.prev_node = current_node.prev_node
                    current_node.prev_node.next_node = new_node
                    current_node.prev_node = new_node
                    break
                count += 1
                current_node = current_node.next_node
            return f'Теперь по индексу {index} данные {new_node.data}'

    def contains_from_head(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next_node
        return False

    def contains_from_tail(self, data):
        current_node = self.tail
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.prev_node
        return False

    def contains_from(self, data, from_head=True):
        if from_head is True:
            return self.contains_from_head(data)
        else:
            return self.contains_from_tail(data)

    def print_ll_from_tail(self):
        current_node = self.tail
        while current_node:
            print(current_node.data)
            current_node = current_node.prev_node
        return "Список выведен с конца"

    def remove_node_index(self, index):
        if index == 0:
            return self.remove_from_head()
        elif index == self.len_ll() - 1:
            return self.remove_from_tail()
        elif index > self.len_ll() - 1:
            return 'Ничего не удалено'
        current_node = self.head
        current_node_index = 0
        while current_node is not None and current_node_index < index - 1:
            current_node = current_node.next_node
            current_node_index += 1
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        current_node.next_node.prev_node = current_node
        return f"Удален узел с данными {removed_node.data} по индексу {index}"

    def remove_node_data(self, data):
        if self.head.data == data:
            return self.remove_from_head()
        elif self.tail.data == data:
            return self.remove_from_tail()
        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.data == data:
                removed_node = current_node.next_node
                current_node.next_node = current_node.next_node.next_node
                current_node.next_node.prev_node = current_node
                return f"Удален узел с данными {removed_node.data}"
            current_node = current_node.next_node
        return 'Ничего не удалено'

    def len_ll(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count


my_list = MyLinkedList()

print(my_list.insert_at_tail(0))
print(my_list.insert_at_tail(1))
print(my_list.insert_at_tail(2))
print(my_list.insert_at_tail(4))
print(my_list.insert_at_tail(5))
print(my_list.insert_at_index(3, 3))
# print(my_list.len_ll())
my_list.print_ll_from_head()
print()
# my_list.print_ll_from_tail()
# print(my_list.contains_from_head(1))
# print(my_list.contains_from(0, from_head=False))
# print(my_list.remove_node_index(3))
# print(my_list.remove_node_data(30))
my_list.print_ll_from_head()
print()
my_list.print_ll_from_tail()
