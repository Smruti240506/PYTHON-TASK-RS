
angles = [30, -15, 45, 200, 60, 90]

def valid_angle(angle):
    return angle >= 0 and angle <= 180

def convert_to_servo(angle):
    return angle * 10

valid_angles = list(filter(valid_angle, angles))

servo_commands = list(map(convert_to_servo, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)
