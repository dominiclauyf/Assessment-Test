def process_and_print_data(
    names: list[str], user_info: list[list[int, float]], skips: list[str] = []
):
    for i, name in enumerate(names):
        if name in skips:
            continue
        print(
            f"{name} is {user_info[0][i]} years old and his height is {user_info[1][i]}ft."
        )


if __name__ == '__main__':
    names = ["Ali", "Hamza", "Usman"]
    user_info = [[23, 29, 32], [5.8, 5.9, 6.1]]
    names = eval(input())
    user_info = eval(input())

    process_and_print_data(names, user_info, ['Usman'])
