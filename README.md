# Menu_set_get

Este programa define una estructura básica para elementos de menú en un restaurante. Incluye clases para representar elementos de menú, que pueden ser bebidas, platos principales y aperitivos, con métodos para obtener y establecer sus atributos, así como para calcular el precio total basado en la cantidad y descuentos por bebidas.

## Clases

### `MenuItem`

La clase `MenuItem` representa un elemento general del menú.

#### Atributos

- `_name` (str): El nombre del elemento del menú.
- `_price` (float): El precio del elemento del menú.

#### Métodos

- `get_name() -> str`: Devuelve el nombre del elemento del menú.
- `get_price() -> float`: Devuelve el precio del elemento del menú.
- `set_name(new_name: str)`: Establece un nuevo nombre para el elemento del menú.
- `set_price(new_price: float)`: Establece un nuevo precio para el elemento del menú.
- `calculate_total(quantity: int = 1) -> float`: Calcula el precio total para una cantidad dada del elemento del menú.

### `Beverage`

La clase `Beverage` hereda de `MenuItem` y representa una bebida en el menú.

#### Atributos

- `_size_ml` (int): El tamaño de la bebida en mililitros.
- `_container` (str): El tipo de contenedor de la bebida.

#### Métodos

- `get_size_ml() -> int`: Devuelve el tamaño de la bebida en mililitros.
- `get_container() -> str`: Devuelve el tipo de contenedor de la bebida.

## Ejemplo de uso

```python
# Crear un elemento del menú
item = MenuItem("Hamburguesa", 5.99)
print(item.get_name())  # Output: Hamburguesa
print(item.get_price())  # Output: 5.99
item.set_name("Hamburguesa con queso")
item.set_price(6.99)
print(item.calculate_total(2))  # Output: 13.98

# Crear una bebida
beverage = Beverage("Coca Cola", 1.99, 500, "Botella")
print(beverage.get_name())  # Output: Coca Cola
print(beverage.get_price())  # Output: 1.99
print(beverage.get_size_ml())  # Output: 500
print(beverage.get_container())  # Output: Botella
print(beverage.calculate_total(3))  # Output: 5.97
```

# Shape Module

Este programa define clases para trabajar con puntos, líneas y poder formar así varias figuras geométricas. Incluye clases para representar estos elementos, con métodos para obtener y establecer sus atributos, así como para calcular distancias, áreas y perímetros.

## Clases

### `Point`

La clase `Point` representa un punto en un plano 2D.

#### Atributos

- `_x` (float): La coordenada x del punto.
- `_y` (float): La coordenada y del punto.

#### Métodos

- `set_x(x: float)`: Establece la coordenada x del punto.
- `set_y(y: float)`: Establece la coordenada y del punto.
- `get_x() -> float`: Devuelve la coordenada x del punto.
- `get_y() -> float`: Devuelve la coordenada y del punto.
- `compute_distance(new_point: "Point") -> float`: Calcula la distancia entre el punto actual y otro punto dado.
- `__repr__() -> str`: Devuelve una representación en cadena del punto.

### `Line`

La clase `Line` representa una línea entre dos puntos en un plano 2D.

#### Atributos

- `_start_point` (Point): El punto de inicio de la línea.
- `_end_point` (Point): El punto de fin de la línea.
- `_length` (float): La longitud de la línea, calculada como la distancia entre los puntos de inicio y fin.

#### Métodos

- `get_start_point() -> Point`: Devuelve el punto de inicio de la línea.
- `get_end_point() -> Point`: Devuelve el punto de fin de la línea.
- `get_length() -> float`: Devuelve la longitud de la línea.

### `Shape`

La clase `Shape` es una clase base para definir atributos comunes y métodos para todas las figuras geométricas.

#### Atributos

- `_vertices` (list): Lista de objetos `Point` que representan los vértices de la figura.
- `_edges` (list): Lista de objetos `Line` que representan los bordes de la figura.
- `_edge_lengths` (list): Lista de longitudes de los bordes de la figura.
- `_inner_angles` (list): Lista de ángulos internos de la figura.
- `_is_regular` (bool): Indica si la figura es regular (todos los lados y ángulos son iguales).

#### Métodos

- `edges() -> list`: Calcula y devuelve la lista de bordes de la figura.
- `regular() -> bool`: Verifica si la figura es regular.
- `compute_area()`: Método abstracto para calcular el área de la figura.
- `compute_perimeter()`: Método abstracto para calcular el perímetro de la figura.
- `compute_inner_angles() -> list`: Calcula y devuelve la lista de ángulos internos de la figura.
- `calculate_angle(a: float, b: float, c: float) -> float`: Calcula un ángulo dado tres lados usando la ley de cosenos.
- `get_vertices() -> list`: Devuelve la lista de vértices de la figura.
- `get_edges() -> list`: Devuelve la lista de bordes de la figura.
- `get_edge_lengths() -> list`: Devuelve la lista de longitudes de los bordes de la figura.
- `get_inner_angles() -> list`: Devuelve la lista de ángulos internos de la figura.
- `get_is_regular() -> bool`: Devuelve si la figura es regular.

### `Rectangle`

La clase `Rectangle` hereda de `Shape` y representa un rectángulo en un plano 2D.

#### Atributos

- `_width` (float): El ancho del rectángulo.
- `_height` (float): La altura del rectángulo.

#### Métodos

- `get_width() -> float`: Devuelve el ancho del rectángulo.
- `get_height() -> float`: Devuelve la altura del rectángulo.
- `compute_area() -> float`: Calcula y devuelve el área del rectángulo.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del rectángulo.

### `Square`

La clase `Square` hereda de `Rectangle` y representa un cuadrado en un plano 2D.

#### Atributos

- `_side` (float): La longitud del lado del cuadrado.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del cuadrado.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del cuadrado.

### `Triangle`

La clase `Triangle` hereda de `Shape` y representa un triángulo en un plano 2D.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del triángulo.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del triángulo.

### `Equilateral`

La clase `Equilateral` hereda de `Triangle` y representa un triángulo equilátero en un plano 2D.

#### Atributos

- `_side` (float): La longitud del lado del triángulo equilátero.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del triángulo equilátero.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del triángulo equilátero.

### `Isosceles`

La clase `Isosceles` hereda de `Triangle` y representa un triángulo isósceles en un plano 2D.

#### Atributos

- `_base` (float): La longitud de la base del triángulo isósceles.
- `_side` (float): La longitud de los lados iguales del triángulo isósceles.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del triángulo isósceles.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del triángulo isósceles.

### `Scalene`

La clase `Scalene` hereda de `Triangle` y representa un triángulo escaleno en un plano 2D.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del triángulo escaleno.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del triángulo escaleno.

### `RightTriangle`

La clase `RightTriangle` hereda de `Triangle` y representa un triángulo rectángulo en un plano 2D.

#### Atributos

- `_base` (float): La longitud de la base del triángulo rectángulo.
- `_height` (float): La longitud de la altura del triángulo rectángulo.

#### Métodos

- `compute_area() -> float`: Calcula y devuelve el área del triángulo rectángulo.
- `compute_perimeter() -> float`: Calcula y devuelve el perímetro del triángulo rectángulo.

## Ejemplo de uso

```python
# Crear puntos
p1 = Point(0, 0)
p2 = Point(3, 4)

# Imprimir puntos
print(p1)  # Output: Point(x=0, y=0)
print(p2)  # Output: Point(x=3, y=4)

# Calcular distancia entre puntos
distancia = p1.compute_distance(p2)
print(f"Distancia entre p1 y p2: {distancia}")  # Output: Distancia entre p1 y p2: 5.0

# Crear una línea
linea = Line(p1, p2)

# Imprimir línea
print(f"Línea desde {linea.get_start_point()} hasta {linea.get_end_point()}, longitud: {linea.get_length()}")  
# Output: Línea desde Point(x=0, y=0) hasta Point(x=3, y=4), longitud: 5.0

# Crear un rectángulo
bottom_left = Point(0, 0)
width = 4
height = 3
rectangle = Rectangle(bottom_left, width, height)

# Imprimir los atributos del rectángulo
print("Área del rectángulo:", rectangle.compute_area())
print("Perímetro del rectángulo:", rectangle.compute_perimeter())
print("Vértices:", rectangle.get_vertices())
print("Bordes:", rectangle.get_edges())
print("Longitudes de los lados:", rectangle.get_edge_lengths())
print("Ángulos internos:", rectangle.get_inner_angles())

# Crear un cuadrado
square = Square(bottom_left, 4)

# Imprimir los atributos del cuadrado
print("Área del cuadrado:", square.compute_area())
print("Perímetro del cuadrado:", square.compute_perimeter())
print("Vértices:", square.get_vertices())
print("Bordes:", square.get_edges())
print("Longitudes de los lados:", square.get_edge_lengths())
print("Ángulos internos:", square.get_inner_angles())

# Crear un triángulo equilátero
equilateral = Equilateral(Point(0, 0), 5)

# Imprimir los atributos del triángulo equilátero
print("Área del triángulo equilátero:", equilateral.compute_area())
print("Perímetro del triángulo equilátero:", equilateral.compute_perimeter())
print("Vértices:", equilateral.get_vertices())
print("Bordes:", equilateral.get_edges())
print("Longitudes de los lados:", equilateral.get_edge_lengths())
print("Ángulos internos:", equilateral.get_inner_angles())

# Crear un triángulo isósceles
isosceles = Isosceles(Point(0, 0), 4, 5)

# Imprimir los atributos del triángulo isósceles
print("Área del triángulo isósceles:", isosceles.compute_area())
print("Perímetro del triángulo isósceles:", isosceles.compute_perimeter())
print("Vértices:", isosceles.get_vertices())
print("Bordes:", isosceles.get_edges())
print("Longitudes de los lados:", isosceles.get_edge_lengths())
print("Ángulos internos:", isosceles.get_inner_angles())

# Crear un triángulo escaleno
scalene = Scalene(Point(0, 0), Point(3, 0), Point(2, 4))

# Imprimir los atributos del triángulo escaleno
print("Área del triángulo escaleno:", scalene.compute_area())
print("Perímetro del triángulo escaleno:", scalene.compute_perimeter())
print("Vértices:", scalene.get_vertices())
print("Bordes:", scalene.get_edges())
print("Longitudes de los lados:", scalene.get_edge_lengths())
print("Ángulos internos:", scalene.get_inner_angles())

# Crear un triángulo rectángulo
right_triangle = RightTriangle(Point(0, 0), 3, 4)

# Imprimir los atributos del triángulo rectángulo
print("Área del triángulo rectángulo:", right_triangle.compute_area())
print("Perímetro del triángulo rectángulo:", right_triangle.compute_perimeter())
print("Vértices:", right_triangle.get_vertices())
print("Bordes:", right_triangle.get_edges())
print("Longitudes de los lados:", right_triangle.get_edge_lengths())
print("Ángulos internos:", right_triangle.get_inner_angles())
