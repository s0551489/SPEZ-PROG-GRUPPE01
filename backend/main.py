from backend.car import *
from backend.customer import Customer
from backend.booking import Booking
from time import sleep
from pathlib import Path
import os

ROOT = Path(__file__).parent.parent

car_file = os.path.join(ROOT, "test_data/car_data.json")
customer_file = os.path.join(ROOT, "test_data/customer_data.json")

with open(car_file) as json_file:
    cars_data = json.load(json_file)

with open(customer_file) as json_file:
    customer_data = json.load(json_file)

cars = Cars()
for i in cars_data.values():
    cars.addCar(i)

customers = Customer()
for i in customer_data.values():
    customers.addCustomer(i)

bookings = Bookings()

customer1 = Customer(customers[1]["surname"], customers[1]["name"], customers[1]["driver_license"],
                     customers[1]["payment_methods"], customers[1]["renting"])
car1 = Car(cars[0]["color"], cars[0]["brand"], cars[0]["model"], cars[0]["seats"], cars[0]["location"],
           cars[0]["price"], cars[0]["available"])

print(customer1.__str__())
print(car1.__str__())

customer1.rentCar(car1)

print(customer1.__str__())
print(car1.__str__())

booking1 = Booking(car1.getID(), customer1.getID())
car1.addBooking(booking1)
customer1.addBooking(booking1)

sleep(5)

customer1.returnCar(car1, booking1)
bookings.append(booking1)
print(booking1.__str__())

for i in bookings:
    print(i)

print(customer1.__str__())
print(car1.__str__())

print(customer1.toJSON())