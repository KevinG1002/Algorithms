def integer_division(a: int, b: int):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    return count


if __name__ == "__main__":
    print(integer_division(10, 2))
