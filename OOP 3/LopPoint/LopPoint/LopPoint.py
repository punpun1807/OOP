
import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # nhập tọa độ
    def input(self):
        self.x = int(input("Nhap x: "))
        self.y = int(input("Nhap y: "))

    # hiển thị tọa độ
    def display(self):
        print(f"({self.x}, {self.y})")

    # tạo điểm đối xứng qua gốc O
    def symmetric(self):
        return Point(-self.x, -self.y)

    # khoảng cách đến gốc O
    def distance_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    # khoảng cách đến điểm khác
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


# Tạo điểm A(3,4)
A = Point(3,4)
print("Diem A:")
A.display()

# Tạo điểm B từ bàn phím
B = Point()
print("Nhap diem B:")
B.input()
print("Diem B:")
B.display()

# Tạo điểm C đối xứng của B
C = B.symmetric()
print("Diem C doi xung B qua O:")
C.display()

# Khoảng cách B đến O
print("Khoang cach B den O:", B.distance_to_origin())

# Khoảng cách A đến B
print("Khoang cach A den B:", A.distance_to(B))