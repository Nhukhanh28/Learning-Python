# Cơ chế hoạt động của "while" trong Python
a = 0
while a < 5:
    print(a)
    a = a + 1 # Dòng này quan trọng để tránh vòng lặp vô hạn

#1 Lệnh điều khiển vòng lặp
i = 1 
while True:
    print(i)
    if i == 5:
        break
    i = i + 1

#2 Mệnh đề else trong while
i = 0 
while i < 10:
    print(i)
    i = i + 1
else:
    print("Vòng lặp kết thúc")



