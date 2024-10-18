#print("toi se di nga vao nam", 2024)
#print(22+8)

#name = input("ban ten la gi")
#print(type(name))

#a = int(input("nhap vao so dau tien: "))
#b = int(input("nhap vao so thu hai: "))

#c = a + b
#d = a - b
#e = a * b
#f = a / b

#print("Tong 2 so", c)
#print("Hieu 2 so", d)
#print("Divided", e)
#print("multiplied", f)


#for i in range(1,12,2):
#    print(i, end="")


#input()

def tong_cac_so_le(n):
    tong = 0
    for i in range(1, n+1, 2):
        tong += i
    return tong

def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def cac_uoc_so(n):
    uoc_so = []
    for i in range(1, n + 1):
        if n % i == 0:
            uoc_so.append(i)
    return uoc_so

# Nhập vào một số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng các số lẻ từ 1 đến n
tong_le = tong_cac_so_le(n)
print(f"Tổng các số lẻ từ 1 đến {n} là: {tong_le}")

# Kiểm tra n có phải số nguyên tố không
if la_so_nguyen_to(n):
    print(f"{n} là số nguyên tố.")
else:
    print(f"{n} không phải là số nguyên tố.")

# In ra các ước số của n
uoc_so = cac_uoc_so(n)
print(f"Các ước số của {n} là: {uoc_so}")



n = int(input("Nhap so nguyen duong n: "))
tong = 0
    for i in range(1, n+1, 2):
        tong += i
    return tong