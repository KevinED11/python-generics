from typing import TypeVar


T = TypeVar("T")


def get_last_item(items: list[T]) -> T:
    return items[-1]


def get_last_item2[T](items: list[T]) -> T:
    return items[len(items) - 1]


def main() -> None:
    elements: list[int] = [1, 2, 3]
    print(get_last_item(elements))

    print(get_last_item2(elements))


if __name__ == "__main__":
    main()
