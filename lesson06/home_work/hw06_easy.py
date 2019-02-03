import math


# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# # Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Решение задачи-1
class Triangle:
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def _side_lengths(self):
        return math.sqrt((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2), \
               math.sqrt((self.point2[0] - self.point3[0])**2 + (self.point2[1] - self.point3[1])**2), \
               math.sqrt((self.point1[0] - self.point3[0])**2 + (self.point1[1] - self.point3[1])**2)

    def _corners(self):
        side_lengths = self._side_lengths()
        corner1 = math.acos((side_lengths[0]**2 + side_lengths[2]**2 - side_lengths[1]**2)
                            / 2 / side_lengths[0] / side_lengths[2])
        corner2 = math.acos((side_lengths[0]**2 + side_lengths[1]**2 - side_lengths[2]**2)
                            / 2 / side_lengths[0] / side_lengths[1])
        corner3 = math.pi - corner1 - corner2

        return corner1, corner2, corner3

    def heights(self):
        corners = self._corners()
        side_lengths = self._side_lengths()

        return tuple([side_lengths[i] * math.sin(corners[i]) for i in range(3)])

    def perimeter(self):
        return sum(self._side_lengths())

    def square(self):
        return self._side_lengths()[2] * self.heights()[0] / 2


triangle1 = Triangle((10, 10), (20, 30), (25, 5))
triangle1_heights = triangle1.heights()
print(f"Высоты треугольника: {triangle1_heights[0]:.2f}, {triangle1_heights[1]:.2f}, {triangle1_heights[2]:.2f}")
print(f"Периметр треугольника: {triangle1.perimeter():.2f}")
print(f"Площадь треугольника: {triangle1.square():.2f}")


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


# Решение задачи-2
class IsoscelesTrapezium:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4

    def _is_parallel(self, point1, point2, point3, point4):
        try:
            return (point1[0] - point2[0]) / (point1[1] - point2[1]) \
                   == (point3[0] - point4[0]) / (point3[1] - point4[1])
        except ZeroDivisionError:
            return point1[1] - point2[1] == point3[1] - point4[1]

    def side_lengths(self):
        return math.sqrt((self.point1[0] - self.point2[0])**2 + (self.point1[1] - self.point2[1])**2), \
               math.sqrt((self.point2[0] - self.point3[0])**2 + (self.point2[1] - self.point3[1])**2), \
               math.sqrt((self.point3[0] - self.point4[0])**2 + (self.point3[1] - self.point4[1])**2), \
               math.sqrt((self.point4[0] - self.point1[0])**2 + (self.point4[1] - self.point1[1])**2)

    def check(self):
        side_lengths = self.side_lengths()
        check1 = self._is_parallel(self.point1, self.point2, self.point3, self.point4) \
                 and not self._is_parallel(self.point2, self.point3, self.point4, self.point1) \
                 and side_lengths[1] == side_lengths[3]
        check2 = not self._is_parallel(self.point1, self.point2, self.point3, self.point4) \
                 and self._is_parallel(self.point2, self.point3, self.point4, self.point1) \
                 and side_lengths[0] == side_lengths[2]

        return check1 or check2

    def perimeter(self):
        return sum(self.side_lengths())

    def square(self):
        side_lengths = self.side_lengths()
        if self._is_parallel(self.point1, self.point2, self.point3, self.point4):
            return (side_lengths[0] + side_lengths[2]) / 2 \
                   * math.sqrt(side_lengths[1]**2 - (side_lengths[0] - side_lengths[2])**2 / 4)
        else:
            return (side_lengths[1] + side_lengths[3]) / 2 \
                   * math.sqrt(side_lengths[0]**2 - (side_lengths[1] - side_lengths[3])**2 / 4)


figure1 = IsoscelesTrapezium((10, 10), (20, 20), (30, 20), (40, 10))
print(f"Фигура {'' if figure1.check() else 'не '}является равнобокой трапецией.")
figure1_side_lengths = figure1.side_lengths()
print(f"Длины сторон фигуры: {figure1_side_lengths[0]:.2f}, {figure1_side_lengths[1]:.2f}, {figure1_side_lengths[2]:.2f}, "
      f"{figure1_side_lengths[3]:.2f}")
print(f"Периметр фигуры: {figure1.perimeter():.2f}")
if figure1.check():
    print(f"Площадь равнобокой трапеции: {figure1.square():.2f}")
