print('Welcome to the tip Calculator')
total = input('What was the total bill? ')
tip = input('How much would you like to tip? 10, 12, or 15%?')
split = input('How many people are splitting the bill?')

total, tip, split = float(total), int(tip), int(split)


total_per_person = (total + (total * (tip/100))) / split

message = f'Each person should pay {total_per_person: .2f}'

print(message)
