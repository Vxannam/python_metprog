import time


def linear_search(arr, element):
    result = []
    for i in range(len(arr)):
        element_arr = arr[i]
        if element_arr == element:
            result.append(element_arr)
    time.sleep(0.01)
    return result

def binary_search(arr, val):
    result = []
    first = 0
    last = len(arr)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last) // 2
        element_arr = arr[mid]
        if element_arr == val:
            index = mid
        else:
            if element_arr > val:
                last = mid - 1
            else:
                first = mid + 1
    if index != -1:
        result.append(arr[index])
        flag_left = True
        k_left = 1
        flag_right = True
        k_right = 1
        while flag_left or flag_right:
            try:
                if flag_left and arr[index - k_left] == val:
                    result.append(arr[index - k_left])
                    k_left += 1
                else:
                    flag_left = False
            except Exception:
                flag_left = False

            try:
                if flag_right and arr[index + k_right] == val:
                    result.append(arr[index + k_right])
                    k_right += 1
                else:
                    flag_right = False
            except Exception:
                flag_right = False
    time.sleep(0.01)
    return result
