from typing import Generic, TypeVar

T = TypeVar("T")


class StackIsEmptyException(Exception):
    pass


class Stack1(Generic[T]):
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: T) -> None:
        self.__items.append(item)

    def pop(self) -> T:
        if self.is_empty:
            raise StackIsEmptyException("Stack is empty")

        return self.__items.pop()

    def __getitem__(self, index: int) -> T:
        if 0 > index >= self.__len__():
            raise IndexError("Index out of range")

        return self.__items[index]

    def __len__(self) -> int:
        return len(self.__items)

    @property
    def is_empty(self) -> bool:
        return len(self.__items) == 0


class Stack2[T]:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: T) -> None:
        self.__items.append(item)

    def pop(self) -> T:
        if self.is_empty:
            raise StackIsEmptyException("Stack is empty")

        return self.__items.pop()

    def __getitem__(self, index: int) -> T:
        if 0 > index >= self.__len__():
            raise IndexError("Index out of range")

        return self.__items[index]

    def __len__(self) -> int:
        return len(self.__items)

    @property
    def is_empty(self) -> bool:
        return len(self.__items) == 0


class Main:
    @staticmethod
    def run() -> None:
        stack: Stack2[int] = Stack2()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        print(stack[-1])


if __name__ == "__main__":
    Main.run()
