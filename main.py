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

    @property
    def is_empty(self) -> bool:
        return len(self.__items) == 0


class Main:
    @staticmethod
    def run() -> None:
        ...


if __name__ == "__main__":
    Main.run()
