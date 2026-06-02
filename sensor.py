def get_sensor_values():
    data = input("Enter 6 sensor values (e.g. 001100): ")

    sensors = list(map(int, data))

    active_sensors = len(list(filter(lambda x: x == 1, sensors)))

    return sensors, active_sensors