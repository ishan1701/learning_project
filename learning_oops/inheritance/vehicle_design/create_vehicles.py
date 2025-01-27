from vehicle_factory import  VehicleFactory

if __name__ == '__main__':
    vehicle=VehicleFactory.create_vehicles(vehicle_type='truck',max_speed=100,seating_capacity=4, model='tata',color='red')
    print(vehicle)

    print(vehicle.__dict__)
    print(vehicle.max_speed)

    print(vehicle.start())
    print(vehicle.stop())

    vehicle=VehicleFactory.create_vehicles(vehicle_type='car', max_speed=250, seating_capacity=6, model='vw', color='black')
    print(vehicle)

    print(vehicle.__dict__)
    print(vehicle.max_speed)

    print(vehicle.start())
    print(vehicle.stop())


