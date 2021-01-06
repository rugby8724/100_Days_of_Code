print('Welcome to the tip Calculator')
total = float(input('What was the total bill? '))
tip = int(input('How much would you like to tip? 10, 12, or 15%?'))
split = int(input('How many people are splitting the bill?'))

total_per_person = (total + (total * (tip/100))) / split

message = f'Each person should pay {total_per_person: .2f}'

print(message)
