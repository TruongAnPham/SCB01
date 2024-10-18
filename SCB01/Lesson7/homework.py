def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

sizes = [100, 1000, 5000, 10000]
for size in sizes:
    arr = [random.randint(0, 10000) for _ in range(size)]
    arr_copy = arr.copy()
    
    insertion_time = measure_time(insertion_sort, arr)
    bubble_time = measure_time(bubble_sort, arr_copy)
    
    print(f"Array size: {size}")
    print(f"Insertion Sort Time: {insertion_time:.6f} seconds")
    print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
    print("-" * 30)