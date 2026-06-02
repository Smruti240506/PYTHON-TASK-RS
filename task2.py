correct_username = "SMRUTI"
correct_password = "1234"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username:
    if password == correct_password:
        print("Login Successful!")
    else:
        print("Incorrect Password!")
else:
    print("Username Not Found!")