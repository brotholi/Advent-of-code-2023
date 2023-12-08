# Created: 12.04.2021 12:00

with open ("input.txt", "r") as f:
    data = f.readlines()

all_numbers = []

for line in data:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char)
    first = numbers[0]
    last = numbers[-1]
    combined = first + last
    all_numbers.append(int(combined))
        
summa = sum(all_numbers)
print(summa)
       
