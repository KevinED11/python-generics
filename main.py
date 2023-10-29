from typing import Generic, TypeVar, Self

T = TypeVar("T")


class StackIsEmptyException(Exception):
    pass


class Stack1(Generic[T]):
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: T) -> Self:
        self.__items.append(item)

        return self

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

    def __repr__(self) -> str:
        return str(self.__items)

    @property
    def is_empty(self) -> bool:
        return len(self.__items) == 0


class Stack2[T]:
    def __init__(self) -> None:
        self.__items = []

    def push(self, item: T) -> Self:
        self.__items.append(item)

        return self

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

    def __repr__(self) -> str:
        return str(self.__items)

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

        new_stack: Stack1[int] = Stack1()
        new_stack.push(1).push(2).push(3).push(4)

        print(new_stack)


if __name__ == "__main__":
    Main.run()
