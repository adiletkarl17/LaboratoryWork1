population = int(input("Enter the population: "))

if population % 2 == 0:
    survivors = population // 2
    print("Number of survivors:", survivors)
else:
    survivors = (population // 2) + 1
    print("Number of survivors:", survivors)