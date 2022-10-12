import time


def insertion_sort(array: list):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while key < array[j] and j > -1:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def selection_sort(array: list):
    n = len(array)


def main():
    print(insertion_sort([3, 2, 0, 4]))


if __name__ == "__main__":
    main()
