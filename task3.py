num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

small = num1 if num1 < num2 else num2

gcd = 1

for i in range(1, small + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd 
        
lcm = (num1 * num2) // gcd

print("GCD =", gcd)
print("LCM =", lcm)