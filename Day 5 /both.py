binary = input("Enter binary number: ")
decimal = int(binary, 2)
print("Binary to Decimal:", decimal)

number = int(input("Enter decimal number: "))
binary = bin(number)[2:]
print("Decimal to Binary:", binary)
