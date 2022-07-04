def sum_recursive(start: int = 1, end: int = 10) -> int:
    if start == end:
        return start
    return end + sum_recursive(start, end - 1)


if __name__ == '__main__':
    print(sum_recursive())
