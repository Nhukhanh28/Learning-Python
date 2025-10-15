# Định nghĩa và gọi hàm 
def chao_mung(ten):
    print(f"Chào mừng {ten} đến với Python!")
    print("Chúc bạn học tập vui vẻ!")
# Gọi hàm
chao_mung("Khanh")

# Giá trị trả về từ hàm 
def tinh_tong(a,b):
    tong = a + b
    return tong
ket_qua = tinh_tong(10,20) # Hàm trả về
print(ket_qua * 2) # Sử dụng giá trị trả về