class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    # Setters
    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    # Getters
    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def compute_distance(self, new_point: "Point"):
        return ((new_point._x - self._x )**2 + (new_point._y - self._y)**2)**0.5

    def __repr__(self):
        return f"Point(x={self.get_x()}, y={self.get_y()})"        

class Line:
    def __init__(self, start_point: Point, end_point: Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = self._start_point.compute_distance(self._end_point)
    
    # Getters
    def get_start_point(self):
        return self._start_point
    
    def get_end_point(self):
        return self._end_point
    
    def get_length(self):
        return self._length
    
    # Setters
    def set_start_point(self, new_start_point):
        self._start_point = new_start_point
    
    def set_end_point(self, new_end_point):
        self._end_point = new_end_point
        
    def __repr__(self):
        return f"Line(start={self.get_start_point()}, end={self.get_end_point()})" 


class Shape:
    """
    Clase principal para definir atributos comunes y métodos para todas las figuras.
    """
    def __init__(self, vertices: list):
        self._vertices = vertices  # lista de objetos Point (vértices)
        self._edges = self.edges()  # lista de objetos Line (bordes)
        self._edge_lengths = [edge.get_length() for edge in self._edges]  # lista de longitudes de los bordes
        self._inner_angles = self.compute_inner_angles()  # lista de ángulos internos
        self._is_regular = self.regular()  # True si la figura es regular, False en caso contrario

    def edges(self):
        edges = []
        self.num_vertices = len(self._vertices)
        for i in range(self.num_vertices):
            edges.append(Line(self._vertices[i], self._vertices[(i + 1) % self.num_vertices]))  # Conecta los vértices y cierra la figura
        return edges

    def regular(self):
        return all(map(lambda length: length == self._edge_lengths[0], self._edge_lengths))

    def compute_area(self):  # Método abstracto para aplicar polimorfismo
        pass

    def compute_perimeter(self):  # Método abstracto para aplicar polimorfismo
        pass

    def compute_inner_angles(self):
        if self.regular():
            angles = (self.num_vertices - 2) * 180 / self.num_vertices
            return [angles] * self.num_vertices
        else:
            angles = []
            for i in range(self.num_vertices):
                a = self._edge_lengths[i - 1]  # Lado anterior
                b = self._edge_lengths[i]      # Lado actual
                c = self._edge_lengths[(i + 1) % self.num_vertices]  # Lado siguiente
                angle = self.calculate_angle(a, b, c)
                angles.append(angle)
            return angles

    def calculate_angle(self, a, b, c):
        import math
        cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
        angle = math.acos(cos_angle)
        return math.degrees(angle)
    
    # Getters
    def get_vertices(self):
        return self._vertices

    def get_inner_angles(self):
        return self._inner_angles

    def get_edge_lengths(self):
        return self._edge_lengths

    def get_edges(self):
        return self._edges
    
    def get_is_regular(self):
        return self._is_regular

    # Setters
    def set_vertices(self, vertices: list):
        self._vertices = vertices

class Rectangle(Shape):
    def __init__(self, point_start: Point, width, height):
        self._width = width
        self._height = height
        vertices = [
            point_start,
            Point(point_start.get_x() + width, point_start.get_y()),
            Point(point_start.get_x() + width, point_start.get_y() + height),
            Point(point_start.get_x(), point_start.get_y() + height)
        ]
        super().__init__(vertices)

    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
     
    def compute_area(self):
        return self.get_width() * self.get_height()

    def compute_perimeter(self):
        return 2 * (self.get_width() + self.get_height())
    
class Square(Rectangle):
    """
    Clase Square que hereda de la clase Rectangle.
    """
    def __init__(self, point_start: Point, side):
        self._side = side
        p1 = point_start
        super().__init__(p1, side, side)
        self._is_regular = True


    def compute_area(self):
        return self._side ** 2

    def compute_perimeter(self):
        return 4 * self._side

    def __repr__(self):
        return f"Square(side={self._side})"
    
class Triangle(Shape):
    """
    Clase Triangle que hereda de la clase Shape.
    """
    def __init__(self, p1: Point, p2: Point, p3: Point):
        vertices = [p1, p2, p3]
        super().__init__(vertices)
        
    def compute_area(self):
        a, b, c = list(map(lambda edge: edge.get_length(), self.get_edges())) #[edge.get_length() for edge in self._edges]
        s = (a + b + c) / 2  # Semi-perimeter
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5  # Heron's formula
    
    def compute_perimeter(self):
        return sum(map(lambda edge: edge.get_length(), self.get_edges()))

    def compute_inner_angles(self):
        a, b, c = [edge.get_length() for edge in self._edges]
        from math import acos, degrees
        angle1 = degrees(acos((b**2 + c**2 - a**2) / (2 * b * c)))
        angle2 = degrees(acos((a**2 + c**2 - b**2) / (2 * a * c)))
        angle3 = 180 - (angle1 + angle2)
        self._inner_angles = [angle1, angle2, angle3]
        return self._inner_angles

class Equilateral(Triangle):
    """
    Triangulo equilátero: Todos los lados y angulos son iguales.
    """
    def __init__(self, point_start: Point, side):
        height = (3**0.5 / 2) * side
        p1 = point_start    
        p2 = Point(side, point_start._y)
        p3 = Point(side / 2, height)
        super().__init__(p1, p2, p3)
        self._is_regular = True

    def __repr__(self):
        return f"Equilateral Triangle(side={self._edges[0].get_length()})"

class Isosceles(Triangle):
    """
    Triangulo isocesles: Dos lados iguales.
    """
    def __init__(self, point_start: Point, base, side):
        height = (side**2 - (base / 2)**2)**0.5
        p1 = point_start
        p2 = Point(base, point_start._y)    
        p3 = Point(base / 2, height)
        super().__init__(p1, p2, p3)
        self._is_regular = False

    def __repr__(self):
        return f"Isosceles Triangle(base={self._edges[0].get_length()}, side={self._edges[1].get_length()})"
    
class Scalene(Triangle):
    """
    Triangulo escaleno: Todos sus lados son distintos.
    """
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__(p1, p2, p3)
        self._is_regular = False

class TriRectangle(Triangle):
    """
    Triangulo rectangulo: Uno de sus angulos es 90°.
    """
    def __init__(self, point_start: Point, base, height):
        p1 = point_start
        p2 = Point(base, point_start._y)
        p3 = Point(point_start._x , height)
        super().__init__(p1, p2, p3)
        self.is_regular = False

print("RECTÁNGULO") 
rectangle = Rectangle(Point(0, 0), width=4, height=2)

print("Área del rectángulo:", rectangle.compute_area())
print("Perímetro del rectángulo:", rectangle.compute_perimeter())
print("Vértices:", rectangle.get_vertices())
print("Bordes:", rectangle.get_edges())
print("Longitudes de los lados:", rectangle.get_edge_lengths())
print("Ángulos internos:", rectangle.get_inner_angles())

print("\nCUADRADO")
square = Square(Point(0,0), side=5)

print("Área del cuadrado:", square.compute_area())
print("Perímetro del cuadrado:", square.compute_perimeter())
print("Vértices:", square.get_vertices())
print("Bordes:", square.get_edges())
print("Longitudes de los lados:", square.get_edge_lengths())
print("Ángulos internos:", square.get_inner_angles())

print("\nTRIÁNGULO")
tri = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))

print("Área del triangulo:", tri.compute_area())
print("Perimetro del triangulo:", tri.compute_perimeter())
print("Vértices:", tri.get_vertices())
print("Bordes:", tri.get_edges())
print("Longitudes de los lados:", tri.get_edge_lengths())
print("Ángulos internos:", tri.get_inner_angles())

print("\nTRIÁNGULO EQUILÁTERO")
eq = Equilateral(Point(0, 0), side=5)

print("Área de un triangulo equilátero:", eq.compute_area())
print("Perimetro de un triangulo equilátero:", eq.compute_perimeter())
print("Vértices:", eq.get_vertices())
print("Bordes:", eq.get_edges())    
print("Longitudes de los lados:", eq.get_edge_lengths())
print("Ángulos internos:", eq.get_inner_angles())

print("\nTRIÁNGULO ISOSCELES")
iso = Isosceles(Point(0, 0), base=4, side=5)

print("Área del triangulo isosceles:", iso.compute_area())
print("Perimetro de un triangulo equilátero:", iso.compute_perimeter())
print("Vértices:", iso.get_vertices())
print("Bordes:", iso.get_edges())
print("Longitudes de los lados:", iso.get_edge_lengths())
print("Ángulos internos:", iso.get_inner_angles())

print("\nTRIÁNGULO ESCALENO")
sca = Scalene(Point(0, 0), Point(4, 0), Point(2, 3))

print("Área del triangulo isosceles:", sca.compute_area())
print("Perimetro de un triangulo equilátero:", sca.compute_perimeter())
print("Vértices:", sca.get_vertices())
print("Bordes:", sca.get_edges())
print("Longitudes de los lados:", sca.get_edge_lengths())
print("Ángulos internos:", sca.get_inner_angles())

print("\nTRIÁNGULO RECTÁNGULO")
tri_rect = TriRectangle(Point(0, 0), base=3, height=4)

print("Área del triangulo isosceles:", tri_rect.compute_area())
print("Perimetro de un triangulo equilátero:", tri_rect.compute_perimeter())
print("Vértices:", tri_rect.get_vertices())
print("Bordes:", tri_rect.get_edges())
print("Longitudes de los lados:", tri_rect.get_edge_lengths())
print("Ángulos internos:", tri_rect.get_inner_angles())
