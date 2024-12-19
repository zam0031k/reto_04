class MenuItem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price
    
    # Getters
    def get_name(self):
        return self._name
    
    def get_price(self):
        return self._price
    
    # Setters
    def set_name(self, new_name):
        self._name = new_name
        
    def set_price(self, new_price):
        self._price = new_price
    
    def calculate_total(self, quantity: int=1):
        """Calculate the total price for a given quantity of the item."""
        return self.get_price()*quantity
    
class Beverage(MenuItem):
    def __init__(self, name: str, price: float, size_ml: int, container: str):
        super().__init__(name, price)
        self._size_ml = size_ml 
        self._container = container  
        
    # Getters
    def get_size_ml(self):
        return self._size_ml
    
    def get_container(self):
        return self._container
    
    # Setters
    def set_size_ml(self, new_size_ml):
        self._size_ml = new_size_ml
        
    def set_container(self, new_container):
        self._container = new_container
        
    def __str__(self):
        return f"{self.get_name()} ({self.get_size_ml()}ml, {self.get_container()}): ${self.get_price():.3f} COP"
        
class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, portion_size: str, sauses:bool):
        super().__init__(name, price)
        self._portion_size = portion_size
        self._sauses = sauses
        
    # Getters
    def get_portion_size(self):
        return self._portion_size
    
    def get_sauses(self):
        return self._sauses
    
    # Setters
    def set_portion_size(self, new_portion_size):
        self._portion_size = new_portion_size
        
    def set_sauses(self, new_sauses):
        self._sauses = new_sauses
    
    def __str__(self):
        return f"{self.get_name()} ({self.get_portion_size()}): ${self.get_price():.3f} COP"
        
class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, porcion_sinze: str, spiciness:bool, sauses:bool):
        super().__init__(name, price)
        self._sinze_portion = porcion_sinze
        self._spiciness = spiciness
        self._sauses = sauses
    
    # Getters
    def get_sinze_portion(self):
        return self._sinze_portion
    
    def get_spiciness(self):
        return self._spiciness
    
    def get_sauses(self):   
        return self._sauses
    
    # Setters
    def set_sinze_portion(self, new_sinze_portion):
        self._sinze_portion = new_sinze_portion
        
    def set_spicinesss(self, new_spiciness):
        self._spiciness = new_spiciness
    
    def set_sauses(self, new_sauses):
        self._sauses = new_sauses
    
    def __str__(self):
        return f"{self.get_name()} ({self.get_sinze_portion()}): ${self.get_price():.3f} COP"
    
class Order:
    def __init__(self):
        self._items = []
        self.total = 0
    
    def add_item(self, item: MenuItem, quantity: int=1):
        """Add an item to the order."""
        self._items.append((item, quantity))
        
    def total_invoice(self):
        """Calculate the total amount for the order."""
        self.total += sum(item.calculate_total(quantity) for item, quantity in self._items)        
        return self.total
    
    def discount_drink(self):
        """
        A discount applies to drinks depending on whether there is a main .
        """ 
        self.discount_beverage = 0
        self.reduction_drink = 0
        self.prices_beverages = 0
        count = 0
        for menu_item, _ in self._items:
            if isinstance(menu_item, MainCourse):
                for menu_item, _ in self._items[count:]:
                    count += 1
                    if isinstance(menu_item, Beverage):
                        self.prices_beverages += menu_item.get_price()
                        self.discount_beverage += 0.20
                        self.reduction_drink = self.prices_beverages * self.discount_beverage
                        break
            else: 
                self.discount_beverage += 0
                self.reduction_drink += 0

    def __str__(self):
        self.total_pay = self.total - self.reduction_drink
        return  (f"The total of the invoice is: ${self.total:.3f} COP\n\n"
                 f"DISCOUNT OF BERVERAGE BY MAIN COURSES: \n"
                 f"-The total price of berverages is: ${self.prices_beverages:.3f} COP \n"
                 f"-The total price of berverages with discount of {self.discount_beverage * 100}% is: ${self.prices_beverages - self.reduction_drink:.3f} COP \n\n"
                 f" The total price to pay is: ${self.total_pay:.3f} COP")

class MedioPago:
  def __init__(self):
    pass

  def pagar(self, order: Order):
    raise NotImplementedError("Subclases deben implementar pagar()")

class Tarjeta(MedioPago):
  def __init__(self, numero, cvv):
    super().__init__()
    self.numero = numero
    self.cvv = cvv

  def pagar(self, order: Order):
    print("Pago con tarjeta: ")
    print(f"Pagando ${order.total_pay:.3f} COP con tarjeta {self.numero[-4:]}")

class Efectivo(MedioPago):
  def __init__(self, monto_entregado):
    super().__init__()
    self.monto_entregado = monto_entregado

  def pagar(self, order: Order):
    print("Pago en efectivo:")
    if self.monto_entregado >= order.total_pay:
      print(f"Pago realizado en efectivo. Cambio: ${(self.monto_entregado - order.total_pay):.3f} COP")
    else:
      print(f"Fondos insuficientes. Faltan ${(order.total_pay - self.monto_entregado):.3f} COP para completar el pago.")

# Create menu items
coca_cola = Beverage("Coca Cola", 3.200, 500, "Bottle")
lemon_juice = Beverage("Lemon Juice", 2.000, 300, "Glass")
nachos = Appetizer("Nachos", 5.000, "Medium", True)
french_fries = Appetizer("French Fries", 4.300, "Small", False)
salad = Appetizer("Fruit Salad", 6.000, "Medium", False)
hamburguer = MainCourse("Hambuerger", 14.000, "Medium", False, True)
pizza = MainCourse("Pizza", 10.000, "Family", False, True)
sushi = MainCourse("Sushi", 13.500, "Large", True, True)
tacos = MainCourse("Tacos", 11.300, "Medium", True, True)

print("MENU:")

# Print each menu item
print(coca_cola)
print(lemon_juice)
print(nachos)
print(hamburguer)
print(pizza)
print(salad)
print(sushi)
print(tacos)

# Create an order
order1 = Order()
order1.add_item(coca_cola, 2)
order1.add_item(french_fries)
order1.add_item(hamburguer)
order1.total_invoice()
order1.discount_drink()
print(f"\nORDER 1: \n{order1}\n")

# Create another order
order2 = Order()
order2.add_item(lemon_juice, 3)
order2.add_item(nachos, 2)
order2.add_item(pizza)
order2.add_item(salad)
order2.total_invoice()
order2.discount_drink()
print(f"ORDER 2: \n{order2}\n")

# Create another order
order3 = Order()
order3.add_item(lemon_juice)
order3.add_item(coca_cola, 3)
order3.add_item(sushi, 2)
order3.add_item(tacos, 3)
order3.add_item(salad)
order3.total_invoice()
order3.discount_drink()
print(f"ORDER 3: \n{order3}\n")

# Pago
pago_orden1 = Tarjeta("1234567890123456", 123)
pago_orden2 = Efectivo(60.000)
pago_orden3 = Efectivo(12.420)

pago_orden1.pagar(order1)
pago_orden2.pagar(order2)
pago_orden3.pagar(order3)
