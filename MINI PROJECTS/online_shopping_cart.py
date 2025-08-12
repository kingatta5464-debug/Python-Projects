class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def show_products(self):
        for p in self.products:
            print(f"Product : {p.name} - Price : {p.price}")

    def total_price(self):
        total = 0
        for p in self.products:
            total += p.price
        print(f"Total Price : {total}")


p1 = product("Shampoo", 539)
p2 = product("Oil", 700)
p3 = product("Cheese", 2400)

c1 = cart()
c1.add_product(p1)
c1.add_product(p2)
c1.add_product(p3)

c1.show_products()
c1.total_price()

c1.remove_product(p2)
print("Cart after removing products : ")
c1.show_products()
print("Total Price after removing products : ")
c1.total_price()
