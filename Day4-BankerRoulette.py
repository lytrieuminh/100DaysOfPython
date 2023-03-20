# Day 4: Banker Roulette

import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

how_many_names = len(names)
random_name = random.randint(0, how_many_names - 1)

# Solution 1:
person_will_pay = names[random_name]
print(person_will_pay + " is going to buy the meal today! Thank you!")

# Another solution:
# person_will_pay = random.choice(names)
# print(person_will_pay + " is going to buy the meal today! Thank you!")
