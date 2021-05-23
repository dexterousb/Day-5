num = int(input("Enter number:"))
power = int(input("Enter power:"))

temp = 1;

while power != 0:
    temp *= num
    power-=1

print(temp)
