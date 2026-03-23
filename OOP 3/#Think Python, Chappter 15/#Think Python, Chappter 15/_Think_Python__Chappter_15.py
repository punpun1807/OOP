import math

class Point:
    """Đại diện cho một điểm trong không gian 2D."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    """Đại diện cho một hình chữ nhật."""
    def __init__(self, width=0, height=0, corner=Point()):
        self.width = width
        self.height = height
        self.corner = corner # corner là một đối tượng Point (góc dưới bên trái)

class Circle:
    """Đại diện cho một hình tròn."""
    def __init__(self, center=Point(), radius=0):
        self.center = center # center là một đối tượng Point
        self.radius = radius

# --- CÁC HÀM XỬ LÝ ---

def distance_between_points(p1, p2):
    """Tính khoảng cách giữa 2 điểm p1 và p2."""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def point_in_circle(circle, point):
    """Kiểm tra điểm có nằm trong hoặc trên biên hình tròn không."""
    d = distance_between_points(circle.center, point)
    return d <= circle.radius

def rect_in_circle(circle, rect):
    """Kiểm tra hình chữ nhật có nằm HOÀN TOÀN trong hình tròn không."""
    # Ta kiểm tra 4 góc của hình chữ nhật
    p1 = rect.corner # Góc dưới trái
    p2 = Point(p1.x + rect.width, p1.y) # Góc dưới phải
    p3 = Point(p1.x, p1.y + rect.height) # Góc trên trái
    p4 = Point(p1.x + rect.width, p1.y + rect.height) # Góc trên phải
    
    # Nếu cả 4 góc đều nằm trong hình tròn thì cả hình chữ nhật nằm trong
    return (point_in_circle(circle, p1) and point_in_circle(circle, p2) and 
            point_in_circle(circle, p3) and point_in_circle(circle, p4))

def rect_circle_overlap(circle, rect):
    """Kiểm tra bất kỳ phần nào của hình chữ nhật có nằm trong hình tròn không."""
    # Cách đơn giản: Kiểm tra xem có bất kỳ góc nào rơi vào trong hình tròn không
    p1 = rect.corner
    p2 = Point(p1.x + rect.width, p1.y)
    p3 = Point(p1.x, p1.y + rect.height)
    p4 = Point(p1.x + rect.width, p1.y + rect.height)
    
    return (point_in_circle(circle, p1) or point_in_circle(circle, p2) or 
            point_in_circle(circle, p3) or point_in_circle(circle, p4))

# --- CHƯƠNG TRÌNH THỬ NGHIỆM ---
# Khởi tạo hình tròn tâm (150, 100), bán kính 75
my_circle = Circle(Point(150, 100), 75)

# Thử nghiệm với một điểm
test_point = Point(160, 110)
print(f"Điểm nằm trong hình tròn: {point_in_circle(my_circle, test_point)}")
