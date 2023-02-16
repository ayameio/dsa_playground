class Node:
        def __init__(self, val) -> None:
            self.value = val
            self.next_node = None
            self.previous_node = None

        def has_next(self) -> bool:
            return self.next_node is not None

        def __str__(self) -> str:
            return f"value: {self.value}"

class LinkedList:
    
    def __init__(self, node: Node) -> None:
        self.head = node
        self.tail = node
        self.length = 1

    def __len__(self) -> int:
        length = 1
        current_node = self.head
        while current_node.has_next() is True:
            length += 1
            current_node = current_node.next_node
        return length

    def __repr__(self) -> str:
        pass

    def insert_at(self, node: Node, index: int):
        current_index = 0
        current_node = self.head

        while current_index < index:
            current_index += 1
            current_node = current_node.next_node

        current_node.next_node = node
        self.length += 1

    def append(self, node: Node):
        print(f"Appending {node.value}")
        tail_before_appending = self.tail
        node.previous_node = tail_before_appending
        self.tail = node

        self.length += 1

    def prepend(self, node: Node):
        print(f"Prepending {node.value}")
        # store current head node
        head_before_prepending = self.head

        # set new node as head
        self.head = node

        # set previous head node as next node of current head node
        self.head.next_node = head_before_prepending
        
        # increment length of our linked list
        self.length += 1

    def remove(self, item: Node):
        pass

    def remove_at(self, index: int):
        current_index = 0
        current_node = self.head
        while current_index < index:
            current_index += 1
            current_node = current_node.next_node

    def get_node(self, index: int) -> Node:
        current_index = 0
        current_node = self.head

        while current_index < index:
            current_index += 1
            current_node = current_node.next_node

        return current_node

def main():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    linked_list = LinkedList(node_1)

    linked_list.append(node_2)
    linked_list.append(node_3)
    linked_list.append(node_4)

    print(linked_list.length)

if __name__ == "__main__":
    main()