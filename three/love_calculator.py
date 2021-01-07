
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true = 'true'
love = 'love'
count = 0
name = name1.lower()+name2.lower()

for l in name:
  if l in true:
    count += 10

for l in name:
  if l in love:
    count += 1

if count < 10 or count > 90:
  print(f'Your score is {count}, you go together like coke and mentos.')
elif count >= 40 and count <= 50:
  print(f'Your score is {count}, you are alright together.')
else:
  print(f'Your score is {count}')
