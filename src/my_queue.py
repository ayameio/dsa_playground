class Node:
    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def has_next(self) -> bool:
        return self.next is not None

    def __str__(self) -> str:
        return f"value: {self.value}"

class MyQueue:
    def __init__(self, node: Node) -> None:
        self.head = node
        self.tail = self.head
        self.length = 1

    def enqueue(self, node):
        self.tail.next = node
        self.tail = node

        print(f"Enqueuing {node}. | Current head: {self.head} | Next in Queue: {self.head.next} | New tail: {self.tail}")

    def dequeue(self) -> Node:
        dequeued_node = self.head
        
        # set new head value
        self.head = self.head.next
        self.length -= 1

        print(f"Dequeuing {dequeued_node}. | New head: {self.head} | Next in Queue: {self.head.next} | Current tail: {self.tail}")
        return dequeued_node

    def peek(self) -> Node:
        return self.head

def main():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)
    node_4 = Node(4)
    node_5 = Node(5)

    my_queue = MyQueue(node_1)
    my_queue.enqueue(node_2)
    my_queue.enqueue(node_3)
    
    my_queue.dequeue()
    my_queue.dequeue()
    
    # my_queue.enqueue(node_4)

    # my_queue.dequeue()


if __name__ == "__main__":
    main()