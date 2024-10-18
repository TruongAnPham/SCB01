n = int(input("Nhap so nguyen duong n: "))

# Tính tổng các số lẻ từ 1 đến n
s = 0
for i in range(1, n + 1, 2):
    s += i
print("Tong cac so le tu 1 den", n, "la", s)

# Kiểm tra xem n có phải là số nguyên tố không
b = True
if n < 2:
    b = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b = False
            break

if b:
    print(n, "la so nguyen to.")
else:
    print(n, "khong phai la so nguyen to.")

# In ra các ước số của n
print("Cac uoc so cua", n, "la: ", end="")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")

