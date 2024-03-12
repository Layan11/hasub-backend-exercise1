
class Item:
    def __init__(self, weight, name):
        self.weight = weight
        self.name = name

    def get_weight(self):
        return self.weight


class Brand:
    def __init__(self, brand):
        self.brand = brand


class Price:
    def __init__(self, price):
        self.price = price


class Color:
    def __init__(self, color):
        self.color = color


class UniversalCharger(Item, Brand, Color, Price):
    def __init__(self):
        Item.__init__(12, "universal charger")
        Brand.__init__("lenovo")
        Color.__init__("black")
        Price.__init__(50)
        self.size = "medium"


class Imported:
    def __init__(self, country):
        self.country = country


class Passport(Item, Color, Price, Imported):
    def __init__(self):
        Item.__init__(1, "passport")
        Color.__init__("blue")
        Price.__init__(50)
        Imported.__init__("USA")


class Display:
    def __init__(self, display):
        self.display = display


class Storage:
    def __init__(self, storage):
        self.storage = storage


class Materials:
    def __init__(self, materials):
        self.materials = materials


class Sunglasses(Item, Color):
    def __init__(self):
        Item.__init__(10, "sunglasses")
        Color.__init__("black")
        self.origin = "italy"
        self.have_case = "yes"


class Sneakers(Item, Brand, Imported):
    def __init__(self):
        Item.__init__(14, "sneakers")
        Brand.__init__("New Balance")
        Imported.__init__("Spain")
        self.new = "false"


class Smartphone(Item, Brand, Display, Storage, Materials):
    def __init__(self):
        Item.__init__(100, "smartphone")
        Brand.__init__("Apple")
        Display.__init__("AMOLED")
        Storage.__init__("128 GB")
        Materials.__init__("lithium, plastic")
        self.OS = "IOS"
        self.camera = "Dual Lens"


class Laptop(Item, Brand, Storage):
    def __init__(self):
        Item.__init__(60, "laptop")
        Brand.__init__("Dell")
        Storage.__init__("512 GB SSD")
        self.processor = "Intel i7"
        self.RAM = "16 GB"
        self.graphics = "NVIDIA GeForce4"


class Smartwatch(Item, Brand, Display):
    def __init__(self):
        Item.__init__(44, "smartwatch")
        Brand.__init__("Samsung")
        Display.__init__("Touchscreen")
        self.battery_life = "3 days"
        self.fitness_features = "Heart Rate Monitor"
        self.connectivity = "Bluetooth"


class Campus(Item, Brand, Price, Materials):
    def __init__(self):
        Item.__init__(4, "campus")
        Brand.__init__("Samsung")
        Price.__init__(50)
        Materials.__init__("iron, plastic")
        self.accuracy = "high"


class Pack:
    def __init__(self, items_list, max_weight, unused_items, max_items):
        self.items_list = items_list
        self.curr_weight = 0
        self.max_weight = max_weight
        self.unused_items = unused_items
        self.total_items = 0
        self.max_items = max_items

    def add_item(self, item):
        new_weight = self.curr_weight + item.get_weight(item)
        if self.total_items == self.max_items:
            print("Reached total items capacity, can't add more items.")
            return
        if new_weight <= self.max_weight:
            self.items_list.append(item)
            self.curr_weight = new_weight
            self.unused_items.pop(item.name)
            self.total_items += 1
            print("Item added successfully!")
        else:
            print("Can't add item, the total wight would surpass the max weight possible.")

    def remove_item(self, item_name):
        if not self.items_list:
            print("Removing item faild!")
            return
        for i in self.items_list:
            if i.name == item_name:
                self.items_list.remove(i)
                self.curr_weight -= i.weight
                self.unused_items[item_name] = i
                self.total_items -= 1
                print("Item removed successfully!")
                return

    def not_full(self):
        return True if self.curr_weight <= self.max_weight and self.total_items <= self.max_items else False

    def get_items(self):
        items_names = []
        for item in self.items_list:
            items_names.append(item.name)
        return items_names

    def print_items(self):
        print(self.items_list)


if __name__ == '__main__':
    max_total = 80
    max_items = 6
    items = {"universal charger":UniversalCharger, "passport":Passport, "sunglasses":Sunglasses,
             "sneakers":Sneakers, "smartphone":Smartphone, "laptop":Laptop, "smartwatch":Smartwatch, "campus":Campus}
    pack = Pack([], max_total, items, max_items)

    while pack.not_full():
        print("Curr packing list is: ")
        pack.print_items()
        print("Total weight left to fill = " + str(pack.max_weight - pack.curr_weight))
        op = '-1. vars, logic, conditions'
        while op not in ['1. vars, logic, conditions', '0']:
            op = input(print("press '1. vars, logic, conditions' to add item, and '0' to remove: "))
        if op == '1. vars, logic, conditions':
            new_item = ""
            unused_names = pack.unused_items.keys()

            print("Choose item to add from: ")
            print(unused_names)
            while new_item not in unused_names:
                new_item = input(print("Choose item from the list showed above: "))
            print("IN HERE")
            print(pack.unused_items[new_item])
            pack.add_item(pack.unused_items[new_item])
        else:
            print("Choose item to remove from: ")
            print(pack.items_list)
            remove_item = ""
            used_names = pack.get_items()
            if not used_names:
                print("There are no items to remove.")
            else:
                while remove_item not in used_names:
                    remove_item = input(print("Choose item from the list showed above: "))
                pack.remove_item(remove_item)









