# x = 10
#
# y = x
#
# x = 50
#
# print(x)
#
# print(y)

# file = open("student.txt", "w")
#
# file.write("Name : Pavan\n")
# file.write("Age : 28\n")
# file.write("City : Hyderabad")
#
# file.close()

with open("student.txt", "r") as file:

    print(file.read())

with open("student.txt", "a") as file:

    file.write("\nPhone : 9700355208")


with open("employee.txt", "w") as file:

 file.write("Name :" "Pavan\n")
 file.write("Role :" "Software quality engineer\n")
 file.write("experience :" "6 years")




