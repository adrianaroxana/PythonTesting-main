from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def remaining_gas_distance(self):
        raise NotImplemented

    @abstractmethod
    def distance_time(self):
        raise NotImplemented


class Car(Vehicle):
    def __init__(self, no_gas_lt, speed, distance, gas_waste_avg):
        self._no_gas_lt = no_gas_lt
        self._speed = speed
        self._distance = distance
        self._gas_waste_avg = gas_waste_avg


    def remaining_gas_distance(self):
        return (self._no_gas_lt / self._gas_waste_avg) * 100

    def distance_time(self):
        return self._distance/self._speed


class Hyundai(Car):
    def __init__(self, no_gas_lt, speed, distance, gas_waste_avg, mileage):
        super().__init__(no_gas_lt, speed, distance, gas_waste_avg)
        self._mileage = mileage


    def mileage(self):

        self._mileage += self._distance
        return self._mileage


c1 = Hyundai(30, 70, 300, 9, 1000)
print(c1.mileage())
print(c1.mileage())
print(c1.mileage())