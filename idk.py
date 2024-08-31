theuser = input("Create a username: ")
thepass = input("Create a password: ")


users = [
    (0, theuser, thepass),
    (1, "Rolf", "1234"),

]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password and username_input == username:
    print("Successful login")
else:
    print("Incorrect details")