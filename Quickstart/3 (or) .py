ten_nguoi_dung = input("Nhap ten nguoi dung: ")
# Sử dụng 'Khách' làm tên mặc định nếu ten_nguoi_dung là rỗng
ten_hien_thi = ten_nguoi_dung or "Khach"
print("Chao mung ban," + ten_hien_thi + "!")