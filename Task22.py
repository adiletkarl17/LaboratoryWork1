number = int(input('Enter a number: '))

thousand = number // 1000
hundred = (number // 100) % 10
ten = (number // 10) % 10
position = number % 10

print("The digit in the thousand postion is:", thousand)
print("The digit in the hundred postion is:", hundred)
print("The digit in the ten postion is:", ten)
print("The digit in the postion of units is:", position)