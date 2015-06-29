import sys


def find_max_crossing_subarray(array, low, mid, high):
    left_sum = -sys.maxint
    temp_sum = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        temp_sum += array[i]
        if temp_sum > left_sum:
            left_sum = temp_sum
            max_left = i
    right_sum = -sys.maxint
    temp_sum = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        temp_sum += array[j]
        if temp_sum > right_sum:
            right_sum = temp_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(array, low, high):
    if high == low:
        return low, high, array[low]
    else:
        mid = (low + high) / 2
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(array, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def brute_find_max_subarray(array, low, high):
    max_low = low
    max_high = high
    max_sum = -sys.maxint
    for i in range(low, high + 1):
        temp_sum = 0
        for j in range(i, high + 1):
            temp_sum += array[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
                max_low = i
                max_high = j
    return max_low, max_high, max_sum

# TODO: find n0 point at which the recursive algorithm beats the brute-force algorithm
if __name__ == '__main__':
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4]
    low, high, max_sum = find_max_subarray(array, 0, len(array) - 1)
    print(array[low:high+1], max_sum)
    low, high, max_sum = brute_find_max_subarray(array, 0, len(array) - 1)
    print(array[low:high+1], max_sum)