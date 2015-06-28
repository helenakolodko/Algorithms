__author__ = 'lena'


def sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key



if __name__ == '__main__':
    array = [1, 51, 5, 9, 3, -9, 31, 844, 1, 56, -5, -64, 654]
    sort(array)
    print(array)