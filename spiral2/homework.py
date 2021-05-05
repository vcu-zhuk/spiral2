def spiralize(size, n=1):
    total = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0

    if size == 1:
        total = 1
    while size > 1:
        total1 += size ** 2
        total2 += size ** 2 - (size - 2)
        total3 += size ** 2 - (size - 4)
        total4 += size ** 2 - (size - 6)
        total = total1 + total2 + total3 + total4

    return_value = total
    return return_value


if __name__ == "__main__":
    print(spiralize(501, 15))
