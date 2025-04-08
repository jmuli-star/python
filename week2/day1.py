# f_name= "berlin"
# l_name= "ivy"

# fullname= f_name + " " + l_name
# print(fullname)

# print("mango" in fullname)

file = open("example.txt", "r")
content = file.read()
print(content)

with open("example.txt", "r") as file:
    content = file.readlines()
    print(content)


with open("example2.txt", "w") as file:
    file.write("we are playin quiddditch")

with open("example2.txt", "a") as file:
    file.write("\n oseph muli")