from sensor import get_sensor_values
from movement import decide_movement

sensors, active_sensors = get_sensor_values()

print("Sensor Values:", sensors)
print("Active Sensors:", active_sensors)

action = decide_movement(sensors)

print("Robot Action:", action)