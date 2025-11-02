"""Task 3

Product Store

Write a class Product that has three attributes:

type
name
price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can't perform its action, should raise ValueError with appropriate error information.


Also, the ProductStore class must have the following methods:
- add(product, amount):
    adds a specified quantity of a single product with a predefined price premium for your store(30 percent)

- set_discount(identifier, percent, identifier_type='name'):
    adds a discount for all products specified by input identifiers (type or name).
    The discount must be specified in percentage

- sell_product(product_name, amount):
    removes a particular amount of products from the store if available,
    in other case raises an error. It also increments income if the sell_product method succeeds.

- get_income():
    returns amount of money earned by ProductStore instance.
- get_all_products():
    returns information about all available products in the store.
- get_product_info(product_name):
    returns a tuple with product name and amount of items in the store.
'''

class Product:

    pass

class ProductStore:

pass

p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
'''
"""

# Створюємо клас Продукт для товару
class Product:
   
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __repr__(self):
        return f'Product("{self.type}", "{self.name}", {self.price})'

# Створюємо клас Продуктовий магазин
class ProductStore:

    def __init__(self):
        self.products = {}
        self.prices = {}
        self.product_objects = {}
        self.discounts_by_name = {}
        self.discounts_by_type = {}
        self.total_income = 0
    
    # Додавання товару для магазину
    def add(self, product, amount):
        price_with_markup = product.price * 1.3
        self.prices[product.name] = price_with_markup
        self.product_objects[product.name] = product
        if product.name in self.products:
            self.products[product.name] += amount
        else:
            self.products[product.name] = amount

    # Встановлення знижки для товару
    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            # Перевіряємо чи існує товар з такою назвою
            if identifier not in self.products:
                raise ValueError(f"Product '{identifier}' not found")
            
            # Зберігаємо знижку для цієї назви
            self.discounts_by_name[identifier] = percent
        
        # Перевіряємо чи існує товар з таким типом, якщо не знайшли за назвою   
        elif identifier_type == 'type':
           
            # Встановлюємо знижку для всіх товарів цього типу
            self.discounts_by_type[identifier] = percent
            
        else:
            raise ValueError('Identifier_type must be "name" or "type"')
    
    # Розраховуємо фінальну ціну зі знижкою
    def _get_final_price(self, product_name):
        
        # Ціна з націнкою 30%
        price = self.prices[product_name]
        product = self.product_objects[product_name]
        
        # Шукаємо знижку за назвою
        discount = self.discounts_by_name.get(product_name, 0)
        
        # Якщо немає знижки за назвою - беремо за типом
        if discount == 0:
            discount = self.discounts_by_type.get(product.type, 0)
        
        # Застосовуємо знижку
        final_price = price * (1 - discount / 100)
        
        return final_price
    
    # Продажа товару і додавання доходу
    def sell_product(self, product_name, amount):
        
        # Перевіряємо чи є такий товар
        if product_name not in self.products:
            raise ValueError(f'Product "{product_name}" not found')
        
        # Перевіряємо чи вистачає кількості
        available = self.products[product_name]
        if amount > available:
            raise ValueError(
                f'Not enough product "{product_name}". '
                f'Available: {available}, need: {amount}'
            )
        # Віднімаємо продану кількість та рахуємо дохід
        self.products[product_name] -= amount
        final_price = self._get_final_price(product_name)
        earned = final_price * amount
        self.total_income += earned
    
    # Загальний дохід магазину
    def get_income(self):
        return self.total_income
    
    # Повертає список всіх товарів у магазині
    def get_all_products(self):
        return [(name, amount) for name, amount in self.products.items()]

    # Повертає інформацію про конкретний товар у магазині
    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError(f'Product "{product_name}" not found')
        
        return (product_name, self.products[product_name])




p1 = Product('food', 'bread', 50)
p2 = Product('food', 'bananas', 100)
p3 = Product('auxilary', 'soap', 30)

store = ProductStore()

store.add(p1, 10)
store.add(p2, 300)

print(store.products)
print(store.get_product_info('bananas'))
store.sell_product('bananas', 50)
print(store.get_product_info('bananas'))

# s.sell_product('Ramen', 10)

# assert s.get_product_info('Ramen') == ('Ramen', 290)