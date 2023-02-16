from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
        self.next: Node[T] = None

class MyStack(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, node: Node[T]):
        self.length += 1 

        if self.head is None:
            self.head = node
            return
        
        node.next = self.head
        self.head = node

    def pop(self) -> Node[T]:
        self.length -= 1
        popped = self.head
        self.head = popped.next
        return popped.value

    def peek(self) -> Node[T]:
        return self.head.value

def main():
    node_1 = Node(1)
    node_2 = Node(2)
    node_3 = Node(3)

    my_stack = MyStack()
    my_stack.push(node_1)
    my_stack.push(node_2)
    my_stack.push(node_3)

    my_stack.pop()
    my_stack.pop()

    my_stack.push(node_3)
    return

if __name__ == "__main__":
    main()