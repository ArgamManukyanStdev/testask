import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class Make:
    name: str


@dataclass
class Model:
    name: str


@dataclass
class Vehicle:
    make: Make
    model: Model
    fuel_capacity: int
    fuel_economy: float = 1  # The number of fuel consumption per mile
    fuel_level = 0

    def __post_init__(self):
        if any([self.fuel_capacity < 0, self.fuel_level < 0]):
            raise ValueError("Please set a positive value")
        if self.fuel_economy <= 0:
            raise ValueError("Please set a value greater than 0")

    def validate_distance(self, distance):
        """Distance validator method"""

        if distance < 0:
            raise ValueError("Please set a positive value")
        if self.fuel_level / self.fuel_economy < distance:
            raise ValueError("You cannot reach at the destination")

    def action(self):
        """Action describing for each kind of instance"""
        NotImplemented("Please implement this method")

    @property
    def full_name(self):
        """Returns the vehicle type model and make names"""

        return f"{self.model.name} {self.make.name}"

    def start(self):
        """Vehicle start method"""

        return f"The {self.full_name} is starting."

    def stop(self):
        """Vehicle stop method"""
        return f"The {self.full_name} is stopping."

    def drive(self, distance: float):
        """Vehicle drive method. After distance validation, will be subtracted the necessary liter of fuel"""

        self.validate_distance(distance=distance)
        beginning_fuel_level = self.fuel_level
        self.fuel_level -= self.fuel_economy * distance

        return f"Beginning fuel level was {round(beginning_fuel_level, 2)} and now it is {round(self.fuel_level, 2)} liter."


class FuelProcessor:

    def __init__(self, vehicle: Vehicle):
        self.__refuel_status = False
        self.vehicle = vehicle

    @property
    def refuel_status(self):
        return self.__refuel_status

    @refuel_status.setter
    def refuel_status(self, val):
        self.__refuel_status = val

    @staticmethod
    def validate_amount(amount: float):
        """Validate fuel amount"""

        if amount < 0:
            raise ValueError("Please set positive value")

    def refuel(self, amount: float):
        """Vehicle refuel method"""

        if not getattr(self, "refuel_status", False):
            raise ValueError("Please call `is_allowed_to_refuel` at first then refuel")

        self.validate_amount(amount=amount)

        self.vehicle.fuel_level += amount
        curr_level = self.get_current_level()
        self.refuel_status = False
        return f"Refueled {self.vehicle.full_name}. Current fuel level: {curr_level} liter."

    def get_current_level(self) -> float:
        """Return the current fuel level"""
        return round(self.vehicle.fuel_level / self.vehicle.fuel_capacity, 2)

    def get_current_level_percentage(self):
        """Returns current fuel leve percentage"""
        return round(self.get_current_level() * 100, 2)

    def is_allowed_to_refuel(self, amount: float):
        """Check is the vehicle allowed to fuel"""

        self.validate_amount(amount=amount)
        level = amount + self.vehicle.fuel_level

        if level > self.vehicle.fuel_capacity:
            curr_level = self.get_current_level()
            raise ValueError(f"Cannot refuel beyond capacity. Fuel level: {curr_level} liter.")

        self.refuel_status = True

    def warn_to_fuel(self):
        """whenever fuel level percentage lower than 5% of capacity show warning message"""

        if self.get_current_level_percentage() < 5:
            logger.warning(
                f"You should refuel your {self.vehicle.full_name}, current level: {self.get_current_level()} liter")


@dataclass
class Car(Vehicle):
    trunk_capacity: float = 1
    trunk_items = 0

    def __post_init__(self):
        super().__post_init__()
        if any([self.trunk_capacity < 0, self.trunk_items < 0]):
            raise ValueError("Please set a positive value")

    def action(self):
        return f"Opening the trunk of the {self.full_name}."


@dataclass
class Motorcycle(Vehicle):
    has_sidecar: bool = False

    def action(self):
        return f"The {self.full_name} pops a wheelie!"


def main() -> None:
    car_model = Model(name="Honda")
    car_make = Make(name="Civic")
    motorcycle_model = Model(name="Ducati")
    motorcycle_make = Make(name="Monster")
    #####################################################################
    ############################ Car details ############################
    #####################################################################

    v1 = Car(make=car_make, model=car_model, fuel_capacity=30, trunk_capacity=30, fuel_economy=2)
    fuel_car = FuelProcessor(v1)

    start = v1.start()
    curr_level = fuel_car.get_current_level_percentage()
    act = v1.action()
    stop = v1.stop()
    fuel_car.is_allowed_to_refuel(29)
    fuel_car.refuel(29)
    v1.drive(10.3)
    fl_res = v1.drive(4)  # To raise warning message ("warning light" as noticed in the task)
    fuel_car.warn_to_fuel()

    #####################################################################
    ############################ Motorcycle details ############################
    #####################################################################

    v2 = Motorcycle(make=motorcycle_make, model=motorcycle_model, fuel_capacity=10, has_sidecar=False, fuel_economy=0.5)
    fuel_motorcycle = FuelProcessor(v2)

    moto_start = v2.start()
    moto_curr_level = fuel_motorcycle.get_current_level_percentage()
    fuel_motorcycle.is_allowed_to_refuel(9)
    fuel_motorcycle.refuel(9)
    moto_fl_res = v2.drive(10)
    moto_act = v2.action()
    moto_stop = v2.stop()
    fuel_motorcycle.warn_to_fuel()
    print("CAR DETAILS")
    print(start)
    print("Current fuel level is ->", curr_level)
    print(act)
    print(stop)
    print(fl_res)
    print()
    print()
    print("MOTORCYCLE DETAILS")

    print(moto_start)
    print("Current fuel level is ->", moto_curr_level)
    print(moto_act)
    print(moto_stop)
    print(moto_fl_res)


if __name__ == "__main__":
    # Creating instances of Car and Motorcycle
    main()
