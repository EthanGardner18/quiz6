class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity

    def check_availability(self, item, quantity):
        if item.name in self.items and self.items[item.name] >= quantity:
            return True
        return False
    
    def update_inventory(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] -= quantity

class Order:
    def __init__(self, customer, items, inventory, quantity):
        self.customer = customer
        self.items = items
        self.inventory = inventory
        self.quantity = quantity

    def calculate_order_cost(self):
        total = sum(item.price * self.quantity for item in self.items)
        return total

    def validate_order(self):
        for item in self.items:
            if not self.inventory.check_availability(item, self.quantity):
                return False
        return True

def main():
    customer = Customer("Ethan Gardner", "ethangrdnr@gmail.com", "259 North Seminary Street")
    item_laptop = Item("laptop", 800)
    item_monitor = Item("Monitor", 300)
    item_headset = Item("Headset", 100)

    inventory = Inventory()

    inventory.add_item(item_laptop, 10)
    inventory.add_item(item_headset, 3)
    inventory.add_item(item_monitor, 76)

    order = Order(customer, [item_monitor], inventory, 70)

    if order.validate_order():
        total = order.calculate_order_cost()
        print("Total cost: $" + str(total))
    else:
        print("Couldn't validate order")

if __name__ == "__main__":
    main()

