class Car:
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def start_engine(self):
        print(f"{self.brand} đang khởi động động cơ.")

    def stop_engine(self):
        print(f"{self.brand} đã tắt động cơ.")

    def display_info(self):
        print(f"Thông tin xe: {self.brand}")
        print(f"Màu sắc: {self.color}")
        print(f"Năm sản xuất: {self.year}") 
    
# Tạo đối tượng từ lớp Car
my_car = Car("Toyota", "Đỏ", 2020)

my_car.display_info()
my_car.start_engine()   