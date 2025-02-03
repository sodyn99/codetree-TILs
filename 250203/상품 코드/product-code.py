product_name, product_code = input().split()
product_code = int(product_code)

# Write your code here!

class Product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code
    
    def print_product(self):
        print(f"product {self.code} is {self.name}")

product1 = Product()
product1.print_product()

product2 = Product(product_name, product_code)
product2.print_product()