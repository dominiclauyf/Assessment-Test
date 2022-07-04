def unique_list(l: str) -> str:
    words = l.split(" ")
    return " ".join(sorted(set(words), key=words.index))


if __name__ == '__main__':
    string = input()

    print(unique_list(string))
