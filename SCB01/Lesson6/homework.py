import time

# tuyến tính
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# nhị phân
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



if __name__ == "__main__":
    import random
    
    sizes = [10, 100, 1000, 10000, 100000]
    x = 99999
    
    for size in sizes:
        arr = random.sample(range(1, size * 10), size)  # Tạo mảng ngẫu nhiên không trùng lặp
        arr.sort()  # Mảng cần được sắp xếp trước khi áp dụng binary search
        
        print(f"Kích thước mảng: {size}")
        
        start_time = time.time()
        result = linear_search(arr, x)
        end_time = time.time()
        print(f"Linear Search - Vị trí: {result}, Thời gian: {end_time - start_time} giây")
        
        start_time = time.time()
        result = binary_search(arr, x)
        end_time = time.time()
        print(f"Binary Search - Vị trí: {result}, Thời gian: {end_time - start_time} giây")
        
        print("-" * 50)
