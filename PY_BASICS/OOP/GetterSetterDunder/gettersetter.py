# class Bike:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# class Bike1:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
#
#     def set_price(self, new_price):
#         if new_price > 0:
#             self.price = new_price
#         else:
#             print("Invalid price")


class Bike:
    def __init__(self, brand, price):
        self._price = price   # _ hocchee protected convension
        self.brand = brand    # means use via methods not direct

    # GETTER
    @property
    def get_price(self):
        return self._price

    # SETTER
    @get_price.setter
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            print("Invalid price")

# ***********OP**************

b = Bike("Z900", 10)
print(f"Current bike price is ", b.get_price)   # 10 its a property

# b.set_price = -5      # Invalid price
b.set_price = -12
print(f"After seeting price modified bike price is ", b.get_price)   # 12 its a property


class Bike1:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
b = Bike1("Z900", 10)

print(f"Bike price",b.price)     # 10
b.price = -50      # ❌ allowed
print(b.price)     # -50 (invalid but Python allows)

