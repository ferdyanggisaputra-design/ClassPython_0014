class Rectangle:
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Input value cannot be 0 or less.")
        self.length = length
        self.width = width
    def calculate_circumference(self):
        return 2 * (self.length + self.width)
    def calculate_area(self):
        return self.length * self.width
    def __str__(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"
def main():
    try:
        panjang = 3
        lebar = 2
        my_rectangle = Rectangle(panjang, lebar)
        print(my_rectangle)
        circumference = my_rectangle.calculate_circumference()
        print(f"Circumference: {circumference} cm")
        area = my_rectangle.calculate_area()
        print(f"Area: {area} cm^2")
    except ValueError as e:
        print(f"Error: {e}")
