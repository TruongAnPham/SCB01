# Nhập số lượng học sinh
n = int(input("Nhập số lượng học sinh: "))

# Nhập điểm cho từng học sinh
scores = []
for i in range(n):
    score = float(input(f"Nhập điểm của học sinh thứ {i + 1}: "))
    scores.append(score)

# Tính mean (trung bình)
mean = sum(scores) / n

# Tính median (trung vị)
scores.sort()  # Sắp xếp danh sách điểm
if n % 2 == 0:
    median = (scores[n//2 - 1] + scores[n//2]) / 2
else:
    median = scores[n//2]

# Tính mode (giá trị thường xuất hiện nhất)
mode = max(set(scores), key=scores.count)

# In báo cáo
print("Báo cáo:")
print("Mean (Trung bình): ",mean)
print("Median (Trung vị):",median)
print("Mode (Giá trị thường xuất hiện nhất): ",score)
