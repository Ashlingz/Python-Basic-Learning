class Product:
    id = None
    name = None
    price = None
    qty = None

    def __init__(self, id, name, price, qty):
        self.id = id
        self.name = name
        self.price = price
        self.qty = qty

    def amount(self):
        return self.price * self.qty

    def __str__(self):
        return f'{self.id} {self.name} {self.price:,.2f} {self.qty:,.2f}'