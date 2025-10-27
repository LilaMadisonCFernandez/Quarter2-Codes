age = int(input("Enter your age:"))
sum = 0

for x in range(1, age+1):
    sum += x

print("The sum of all the number from 1 to", age, "is", sum)