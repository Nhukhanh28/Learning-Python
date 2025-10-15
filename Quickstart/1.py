# Toán tử "and" trong Python 
# Toán tử "and" trả về True nếu cả hai biểu thức đều đúng, ngược lại trả về False.
a = 5 
b = 10 
c = 3 

# Cả hai điều kiện đều đúng 
ket_qua_1 = (a < b) and (c < b) # True and True => True
print(ket_qua_1) # Output: True

# Điều kiện thứ hai là False 
ket_qua_2 = (a < b) and (b < c) # True and False => False 
print(ket_qua_2) # Output: False

# Điều kiện thứ nhất là False 
ket_qua_3 = (a > b) and ( a > c) # False and True => False
print(ket_qua_3) #Output: False