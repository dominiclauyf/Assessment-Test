def intersection(lst1: list[int], lst2: list[int]) -> list[int]:
    return list(set(lst1) & set(lst2))


if __name__ == '__main__':
    result = intersection([1, 3, 6, 78, 35, 55], [12, 24, 35, 55, 88, 78, 155])
    print(f"Intersection: {result}")
