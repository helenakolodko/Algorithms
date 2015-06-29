def sort(array, increasing=True):
    sort_subarray(array, 0, len(array) - 1, increasing)

def sort_subarray(array, low, high, increasing=True):
    for j in range(low + 1, high + 1):
        key = array[j]
        i = j - 1
        while i >= 0 and (array[i] > key) == increasing:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

if __name__ == '__main__':
    array = [1, 51, 5, 9, 3, -9, 31, 844, 1, 56, -5, -64, 654]
    sort(array)
    print(array)
    sort(array, False)
    print(array)
