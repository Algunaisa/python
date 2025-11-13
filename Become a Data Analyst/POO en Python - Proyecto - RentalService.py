#RentalService

#vehicle.py
from datetime import datetime, timedelta  

class Vehicle:
    def __init__(self, brand, model, vehicle_type):
        self.brand = brand
        self.model = model
        self.vehicle_type = vehicle_type
        self.is_rented = False
        self.rental_due_date = None

    def rent(self, customer):
        # Allow a customer to rent the vehicle if available
        if not self.is_rented:
            self.is_rented = True
            self.rental_due_date = datetime.now() + timedelta(days=7)
            customer.rented_vehicle = self
            print("%s rented %s %s, due back on %s." % (customer.name, self.brand, self.model, self.rental_due_date.date()))
        else:
            print("%s %s is already rented." % (self.brand, self.model))

    def return_vehicle(self):
        # Return the vehicle and clear the due date
        self.is_rented = False
        self.rental_due_date = None
        print("%s %s has been returned." % (self.brand, self.model))

    def __str__(self):
        return "%s %s (%s)" % (self.brand, self.model, self.vehicle_type)
 
#truck.py
from vehicle import Vehicle

class Truck(Vehicle):
    """A Truck requires a truck license to rent."""
    def rent(self, customer):
        # Prevent renting unless the customer has a truck license
        if customer.has_truck_license:
            Vehicle.rent(self, customer)
        else:
            print("%s cannot rent %s %s without a truck license." % (customer.name, self.brand, self.model))

#customer.py
class Customer:
    def __init__(self, name, has_truck_license=False):
        self.name = name
        self.has_truck_license = has_truck_license
        self.rented_vehicle = None

    def rent_vehicle(self, vehicle):
        # Rent a vehicle if eligible (only one at a time)
        if self.rented_vehicle:
            print("%s already has a rented vehicle and must return it first." % self.name)
        else:
            vehicle.rent(self)

    def return_vehicle(self):
        # Return the currently rented vehicle
        if self.rented_vehicle:
            self.rented_vehicle.return_vehicle()
            self.rented_vehicle = None
        else:
            print("%s has no rented vehicle to return." % self.name)

#rental_service.py
class RentalService:
    def __init__(self):
        self.vehicles = [ ]   # Stores Vehicle objects
        self.customers = [ ]  # Stores Customer objects

    def add_vehicle(self, vehicle):
        # Add a vehicle to the rental system
        self.vehicles.append(vehicle)
        print("Vehicle %s %s added to the rental service." % (vehicle.brand, vehicle.model))

    def list_available_vehicles(self):
        # List all vehicles that are not currently rented
        available = [v for v in self.vehicles if not v.is_rented]
        if available:
            print("\nAvailable Vehicles:")
            for v in available:
                print(v)
        else:
            print("No vehicles available.")

    def add_customer(self, customer):
        # Add a customer to the system
        self.customers.append(customer)
        print("Customer %s added to the rental service." % customer.name)

#main.py
from rental_service import RentalService 
from vehicle import Vehicle
from truck import Truck
from customer import Customer

rental_service = RentalService()

# Add vehicles
car = Vehicle("Toyota", "Camry", "Car")
motorcycle = Vehicle("Honda", "CBR500R", "Motorcycle")
truck = Truck("Ford", "F-150", "Truck")
rental_service.add_vehicle(car)
rental_service.add_vehicle(motorcycle)
rental_service.add_vehicle(truck)

print("\n")

# Add customers
alice = Customer("Alice")
bob = Customer("Bob", has_truck_license=True)
rental_service.add_customer(alice)
rental_service.add_customer(bob)

print("\n")

# Renting vehicles
alice.rent_vehicle(truck)   # Should fail
bob.rent_vehicle(truck)     # Should succeed
alice.rent_vehicle(car)  # Should succeed 

print("\n")

# Returning vehicle and renting again
alice.return_vehicle()
alice.rent_vehicle(motorcycle)  # Now should succeed


# List available vehicles after operations
rental_service.list_available_vehicles()        
            