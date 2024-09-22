N = int(input("Enter the number of schoolchildren: "))
K = int(input("Enter the number of tangerines: "))

tangerins_per_student = K // N
remaining_tanerines = K % N

print(tangerins_per_student)
print(remaining_tanerines)