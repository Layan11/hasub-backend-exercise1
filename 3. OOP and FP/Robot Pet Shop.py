from random import randint


class Robot:
    def __init__(self, main_material, price, cost_to_fix, name, id, battery_type, animal_type, state, days_to_repair):
        self.main_material = main_material
        self.price = price
        self.cost_to_fix = cost_to_fix
        self.name = name
        self.id = id
        self.battery_type = battery_type
        self.animal_type = animal_type
        self.state = state
        self.days_in_repair = 0
        self.days_to_repair = days_to_repair


class Employee(Robot):
    def __init__(self, salary, main_material, price, cost_to_fix, name, id, battery_type, animal_type, state, days_to_repair):
        self.salary = salary
        super().__init__(main_material, price, cost_to_fix, name, id, battery_type, animal_type, state, days_to_repair)


class Store:
    def __init__(self, pets, employees):
        self.pets = pets
        self.balance = 500
        self.employees = employees
        self.in_repair = []

    def find_pet(self, id):
        for pet in self.pets:
            if pet.id == id:
                return pet
        print("pet not found")
        return None

    def print_pet(self, id):
        pet = self.find_pet(id)
        print("Pet name = " + str(pet.name) + " and id = " + str(pet.id) + " details: ")
        print("Pet main material = " + str(pet.main_material))
        print("Pet price = " + str(pet.price))
        print("Pet cost to fix = " + str(pet.cost_to_fix))
        print("Pet battery type = " + str(pet.battery_type))
        print("Pet animal type = " + str(pet.animal_type))
        print("Pet state = " + str(pet.state))

    def buy(self, id):
        pet = self.find_pet(id)
        if not pet:
            return
        if pet.state == "for sale":
            pet.state = "sold"
            self.balance += pet.price

    def for_sale(self):
        for_sale = []
        for pet in self.pets:
            if pet.state == "for sale":
                for_sale.append(pet.name)
        return for_sale

    def print_for_sale(self):
        print("The pets available for sale are: ")
        print(self.for_sale())

    def print_in_repair(self):
        in_repair = []
        for pet in self.pets:
            if pet.state == "in repair":
                in_repair.append(pet.name)
        print("The pets in repair are: ")
        print(in_repair)

    def for_sale_in_range(self, min_price, max_price):
        sale = self.for_sale()
        in_range = []
        for robot in sale:
            if min_price <= robot.price <= max_price:
                in_range.append(robot.name)
        print("The pets for sale and in the given price range are: ")
        print(in_range)

    def print_salaries(self):
        salaries = []
        for employee in self.employees:
            salaries.append([employee.name, employee.salary])
        print("The employees salaries are: ")
        print(salaries)

    def break_pet(self, pet):
        pet.state = "broken"

    def print_balance(self):
        print("The store balance is: " + str(self.balance))

    def fix_broken(self):
        for pet in self.pets:
            if pet.state == "broken":
                self.in_repair.append(pet)
                pet.state = "in repair"

    def new_day(self):
        for pet in self.in_repair:
            self.balance -= pet.cost_to_fix
            pet.days_in_repair += 1
            if pet.days_in_repair == pet.days_to_repair:
                pet.state = "for sale"
                self.in_repair.remove(pet)

        for employee in self.employees:
            self.balance -= employee.salary


def create_pets(num):
    pets = []
    materials = ['iron', 'steel']
    battery = ['lithium', 'alkaline']
    animal_type = ['herbivore', 'carnivore']
    for i in range(num):
        name = "pet " + str(i)
        pet = Robot(materials[randint(2)], randint(20, 70), randint(1, 5), name, i, battery[randint(2)],
                    animal_type[randint(2)], "for sale", randint(6))
        pets.append(pet)
    return pets


def create_employees(num):
    employees = []
    for i in range(num):
        robot = create_pets(1)
        employee = Employee(randint(20, 70), robot.main_materials, robot.price, robot.cost_to_fix, robot.name, robot.id,
                            robot.battery_type, robot.animal_type, robot.state, robot.days_to_repair)
        employees.append(employee)
    return employees


if __name__ == '__main__':
    pets_num = 5
    employees_num = 3
    pets = create_pets(pets_num)
    employees = create_employees(employees_num)
    store = Store(pets, employees)