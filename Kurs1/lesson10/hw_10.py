 #Магазин

class Shop:
    def __init__(self, name, address, open_hours, products=None):
        self._products = products or []
        self.name = name
        self.address = address
        self.open_hours = open_hours
  
    def __str__(self):
        return f'Магазин {self.name} по адресу {self.address} работает {self.open_hours} часа'

    def get_products(self):
        return self._products   

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.id} {self.name} {self.price} {self.quantity}'  

# Наследники
class Fruit(Product):
    def __init__(self, id, name, price, quantity, country, shelf_life):
        super().__init__(id, name, price, quantity)
        self.country = country
        self.shelf_life = shelf_life

    def __str__(self):
        return  f'{self.id} {self.name} {self.price} {self.quantity} {self.country} {self.shelf_life}'



product = Product('1', 'шоколад', '45', '150')
fruit = Fruit(2, 'Банан', '50', '180', 'USA', '15 дней')
a = Shop('Мега', 'ул. Журавлева', '24', products=[str(product), str(fruit)])
print(a)
print(a.get_products())



# Автосалон

class Dealership:
    def __init__(self, name, address, open_hours, cars=None):
        self._cars = cars or []
        self.name = name
        self.address = address
        self.open_hours = open_hours

    def get(self):
        return f'{self.name} {self.address} {self.open_hours}' 

    def get_cars(self):
        return self._cars   

class Car:
    def __init__(self, id, brand, country, year, engine, price):
        self.id = id
        self.brand = brand
        self.country = country
        self.year = year
        self.engine = engine
        self.price = price

    def __str__(self):
        return f'{self.id} {self.brand} {self.country} {self.year} {self.engine} {self.price}'

# Наследники
class Lorry(Car):
    def __init__(self, id, brand, country, year, engine, price, capacity):
        super().__init__(id, brand, country, year, engine, price)
        self.capacity = capacity

    def __str__(self):
        return f'{self.id} {self.brand} {self.country} {self.year} {self.engine} {self.price} {self.capacity}'


