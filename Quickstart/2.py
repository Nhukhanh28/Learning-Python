# Cơ chế ngắt mạch trong toán tử "and"
# Luôn đánh giá biểu thức bên trái trước 
# Nếu biểu thức bên trái là False, thì toàn bộ biểu thức là False

x = 0
y = 10

# Biểu thức bên trái (x < 0) là False
# Python sẽ không đánh giá biểu thức bên phải (y / x)
if (x < 0) and (y / x > 1):
    print ("True")
else:
    print ("False")
    # Output: False