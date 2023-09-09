## Exersice 1
mylist = []
num_stu = int(input("Enter the number of your students: "))

for i in range(num_stu):
    mylist.append(input(f"Enter your {i+1} name: "))


ind = mylist.index("Elina")
print(f"Index of Elina is in {ind}")

print("The end")