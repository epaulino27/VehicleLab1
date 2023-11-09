class Car: #make class Vehicles
    def __init__(self,make,model,year,weight,num_doors): #assign attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors

    def display_info(self):#print out vehicles details neatly
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.weight}")
        print(f"Number of Doors: {self.num_doors}")
        return

    def honk(self):#print a honk sound
        print("Beep!Beep!")

class Boat:
    def __init__(self,make,model,year,weight,boat_type): #assign attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.boat_type = boat_type

    def display_info(self):#print out vehicles details neatly
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.weight}")
        print(f"Boat Type: {self.boat_type}")
        return

    def honk(self):#print a honk sound
        print("BWORRRRRRNK")

class Truck: #make class Vehicles
    def __init__(self,make,model,year,weight,num_doors,payload_capacity): #assign attributes
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

    def display_info(self):#print out vehicles details neatly
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Weight: {self.weight}")
        print(f"Number of Doors: {self.num_doors}")
        print(f"Payload Capacity: {self.payload_capacity}")
        return

    def honk(self):#print a honk sound
        print("Hoonk!")

    def dump_load(self):#print a dumping sound
        print("Clunk!Boom!")

# Test driver code
if __name__ == "__main__":
    # Create instances of Car
    car = Car("Toyota", "Corolla", 2021, 1275.0, 4)
    truck= Truck("Mac", "Street 750", 2019, 220.0, 2, 200)
    boat= Boat("Sea-Doo", "RXT-X",2020,1000,"Fishing Boat")

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the truck
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    truck.dump_load()
    print()

    # Display information of the boat
    print("Boat Info:")
    boat.display_info()
    boat.honk()
    print()
