cars = ["Ford", "Volvo", "BMW"]
print(cars)
print(cars[0])
print(cars[1])
print(cars[2])

print(len(cars))

for x in cars:
    print(x)

cars.append("Honda")
print(cars)

cars.pop(1)
print(cars)

cars.remove("Ford")
print(cars)

# Example: List of test data (usernames)
usernames = ["user1", "user2", "user3"]

# Access the first username
print(usernames[0])  # Output: user1

# Print all usernames
for username in usernames:
    print(username)
