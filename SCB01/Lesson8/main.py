list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]

count = {}

for item in list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

for num, count in count.items():
    print(f"Phần tử {num} xuất hiện {count} lần")

