#tuyen tinh
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

#nhi phan
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


#sap xep danh sach
def sap_xep_danh_sach(arr):

  arr_sorted = []

  while arr:
    max_num = max(arr)
    arr_sorted.append(max_num)
    arr.remove(max_num)

  return arr_sorted

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_list = sap_xep_danh_sach(my_list)
print(sorted_list)


arr = [1,0,30,22,11,44]
def insertion_sort(arr):
  sorted_arr = []
  while arr:
    min = 99999
    for i in arr:
      if i < min:
        min = i
    sorted_arr.append(min)
    arr.remove(min)
  print("Array after sorting", sorted_arr)

insertion_sort(arr)
