def bubble_sort(arr):
    n = len(arr)
    i = 0
    while i < n:
        swapped = False
        j = 0
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            j += 1
        if not swapped:
            break
        i += 1

arr = [64, 34, 25, 12, 22, 11, 90]
print("Mảng ban đầu:", arr)
bubble_sort(arr)
print("Mảng đã sắp xếp:", arr)


list = [9,8,7,6,5,4,3,2,1]
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1): # trừ đi 2 vì khi j + 1 thì sẽ không bị out of range, còn nếu chỉ trừ 1 thì lỗi
            if list[j] > list[j +1]:
                list[j], list[j+1] = list[j+1], list[j]

bubble_sort(list)
print(list)

def intersection(nums1, nums2):
    result = []
    nums1_sorted = sorted(nums1)
    nums2_sorted = sorted(nums2)
    
    i, j = 0, 0
    while i < len(nums1_sorted) and j < len(nums2_sorted):
        if nums1_sorted[i] < nums2_sorted[j]:
            i += 1
        elif nums1_sorted[i] > nums2_sorted[j]:
            j += 1
        else:
            if not result or nums1_sorted[i] != result[-1]:
                result.append(nums1_sorted[i])
            i += 1
            j += 1
    return result

nums1 = [1,8,2,6]
nums2 = [2,7,3,6]
print(intersection(nums1,nums2))






