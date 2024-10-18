
# Nhập số lượng số nguyên
n = int(input("Nhập số lượng các số nguyên:  "))

# Nhập số thứ tự
numbers = []
for i in range(n):
    number = float(input(f"Nhập số thứ {i + 1}: "))
    numbers.append(number)

# Lọc các số chẵn trong danh sách
even_numbers = [num for num in numbers if num % 2 == 0]

# Kiểm tra nếu không có số chẵn nào
if len(even_numbers) == 0:
    print("Không có số chẵn nào trong danh sách.")
else:
    # Tính trung bình cộng các số chẵn
    average_even = sum(even_numbers) / len(even_numbers)
    print(f"Trung bình cộng các số chẵn trong danh sách là: {average_even}")
