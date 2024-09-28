number = int(input())

thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
units = number % 10

print("The digit in the thousands position is", thousands)
print(f"The number in the hundreds position is", hundreds)
print(f"The digit in the tens position is", tens)
print(f"The digit in the position of units is", units)
