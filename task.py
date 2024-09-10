"""

There are some errors and/or bad practices in this code. Please identify them and how to fix.
When reporting any vehicle’s fuel level, please report in percentage.
Please add a function that will:
    Start the given vehicle,
    Show it’s current fuel level
    perform it’s given vehicle-specific action (open trunk if car, pop a wheelie if a motorcycle)
    Stop the given vehicle
We need to expand the function you created in item 3 to account for fuel_economy for different vehicles, along with a method to drive a vehicle a given distance (in miles) and return the fuel level before and after the drive.
Add a ‘warning light’ if any drive will result in the fuel level of a given vehicle going below 5% of the fuel_capacity.


"""


class Vehicle:
    def __init__(self, make, model, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0

    def start(self):
        return f"The {self.make} {self.model} is starting."

    def stop(self):
        return f"The {self.make} {self.model} is stopping."

    def refuel(self, amount):
        if amount + self.fuel_level > self.fuel_capacity:
            return f"Cannot refuel beyond capacity. Fuel level: {self.fuel_level}/{self.fuel_capacity}."
        self.fuel_level += amount
        return f"Refueled {self.make} {self.model}. Current fuel level: {self.fuel_level}/{self.fuel_capacity}."


class Car(Vehicle):
    def __init__(self, make, model, fuel_capacity):
        super().__init__(make, model, fuel_capacity)
        self.trunk_capacity = trunk_capacity
        self.trunk_items = 0

    def open_trunk(self):
        return f"Opening the trunk of the {self.make} {self.model}."


class Motorcycle(Vehicle):
    def __init__(self, make, model, fuel_capacity, has_sidecar=False):
        super().__init__(make, model, fuel_capacity)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        return f"The {make} {model} pops a wheelie!"


if __name__ == "__main__":
    # Creating instances of Car and Motorcycle
    myHondaCivic = Car("Honda", "Civic", 50, 450)
    ducati_monster = Motorcycle("Ducati", "Monster", 20)
