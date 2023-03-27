# Day 5: Adding Even Numbers:

# Option 1:
total1 = 0
for number1 in range(2, 101, 2):
    total1 += number1
print(total1)

# Option 2:
total2 = 0
for number2 in range(1, 101):
    if number2 % 2 == 0:
        total2 += number2
print(total2)
