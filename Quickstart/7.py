# Cơ chế hoạt động của "for" trong Python
#1 Lặp qua một list

trang_trai = ["ga", "cho", "meo"]
for dong_vat in trang_trai:
    print(f"Trong trang trai co: {dong_vat}")

trang_trai = ["ga", "cho", "meo"]
for dong_vat in trang_trai:
    print("Trong trang trai co: " + dong_vat)

#2 Lặp qua một chuỗi 
ten = input("Nhập tên: ")
for ky_tu in ten:
    print(ky_tu)

#3 Lặp theo chỉ mục với range()
    # Lặp 3 lần từ 0 đến 2
for i in range(3):
    print(f"Lần lặp thứ {i + 1}")

#4 Lặp qua chỉ mục và giá trị với enumerate()
mon_an = ["pho", "bun", "com"]
for so_thu_tu, ten_mon in enumerate(mon_an):
    print(f"Món ăn thứ {so_thu_tu + 1} là {ten_mon}")

#5 Lệnh điều khiển vòng lặp
for i in range(10):
    if i == 5:
        break # Dừng vòng lặp khi i = 5
    print(i)

for i in range(5):
    if i % 2 == 0:
        continue # Bỏ qua các số chẵn
    print(i)