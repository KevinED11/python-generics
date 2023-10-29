from typing import Generic, TypeVar, Self
from collections import deque
from queue import LifoQueue


T = TypeVar("T")


class StackIsEmptyException(Exception):
    pass


class Stack1(Generic[T]):
    def __init__(self) -> None:
        self.__items = []

    def push(self, *args: T) -> Self:
        self.__items += args

        return self

    def pop(self) -> T:
        if self.is_empty:
            raise StackIsEmptyException("Stack is empty")

        return self.__items.pop()

    def __getitem__(self, index: int) -> T:
        if index >= self.__len__():
            raise IndexError("Index out of range")

        return self.__items[index]

    def __len__(self) -> int:
        return len(self.__items)

    def __repr__(self) -> str:
        return str(self.__items)

    @property
    def is_empty(self) -> bool:
        return self.__len__() == 0


class Stack2[T]:
    def __init__(self) -> None:
        self.__items = []

    def push(self, *args: T) -> Self:
        self.__items += args

        return self

    def pop(self) -> T:
        if self.is_empty:
            raise StackIsEmptyException("Stack is empty")

        return self.__items.pop()

    def __getitem__(self, index: int) -> T:
        if index >= self.__len__():
            raise StackIsEmptyException("Index out of range")

        return self.__items[index]

    def __len__(self) -> int:
        return len(self.__items)

    def __repr__(self) -> str:
        return str(self.__items)

    @property
    def is_empty(self) -> bool:
        return self.__len__() == 0


class Main:
    @staticmethod
    def run() -> None:
        stack: Stack2[int] = Stack2()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        print(stack[-1])

        new_stack: Stack1[int] = Stack1()
        new_stack.push(1).push(2).push(3).push(4)
        new_stack.push(5, 6, 7, 8, 9, 10)

        print(new_stack)

        # deque is not entirely thread-safe.
        my_stack: deque[int] = deque()
        my_stack.append(1)
        my_stack.append(2)
        my_stack.append(3)

        print(my_stack)

        # LifoQueue is thread-safe
        lifo_queue: LifoQueue[int] = LifoQueue()
        lifo_queue.put(1)
        lifo_queue.put(2)
        lifo_queue.put(3)

        lifo_queue.get()

        print(lifo_queue)


if __name__ == "__main__":
    Main.run()
