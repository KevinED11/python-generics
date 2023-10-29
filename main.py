from typing import Generic, TypeVar


T = TypeVar("T")


class StackIsEmptyException(Exception):
    pass


class Stack1(Generic[T]):
    def __init__(self) -> None:
        self.items = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        if self.is_empty:
            raise StackIsEmptyException("Stack is empty")

        return self.items.pop()

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0


class Main:
    @staticmethod
    def run() -> None:
        ...

if __name__ == "__main__":
    Main.run()
