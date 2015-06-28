def merge(array, start, middle, end):
    left_length = middle + 1
    right_length = end + 1
    left = array[start:left_length]
    right = array[middle+1:right_length]
    i = 0
    j = 0
    for k in range(start, end+1):
        if i < left_length:
            if j < right_length:
                if left[i] <= right[j]:
                    array[k] = left[i]
                    i += 1
                else:
                    array[k] = right[j]
                    j += 1
            else:
                array[k] = left[i]
                i += 1
        else:
            array[k] = right[j]
            j += 1

def sort(array, start, end):
    if start < end:
        middle = (start + end) / 2
        sort(array, start, middle)
        sort(array, middle + 1, end)
        merge(array, start, middle, end)

if __name__ == '__main__':
    array = [1, 51, 5, 9, 3, -9, 31, 844, 1, 56, -5, -64, 654]
    sort(array, 0, len(array)-1)
    print(array)
    # sort(array, False)
    # print(array)