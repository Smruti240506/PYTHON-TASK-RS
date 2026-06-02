
angles = [30, -15, 45, 200, 60, 90]

def is_valid(angle):
    return 0 <= angle <= 180

def servo_command(angle):
    return angle * 10

valid_angles = list(filter(is_valid, angles))

servo_commands = list(map(servo_command, valid_angles))

print("Valid Angles:", valid_angles)
print("Servo Commands:", servo_commands)