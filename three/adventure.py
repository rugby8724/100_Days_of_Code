print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

direction = input('There is a fork in the road\n Do you go left or right?')
lake = ''
door= ''

if direction.lower() == 'left':
  print('You go left and see a large beautiful lake in front of you')
  print('A sign says there will be a ferry in 5 hours. Would you like to wait for the ferry or swim across')
  lake = input('wait or swim?\n')
else:
  print('A head you see a hungry grizzley bear')
  print('You can\'t remember if you should curl into a ball or make yourself seem large')
  print('Which one is it..or wait it\'s to late the grizzly bear is having you for a nice snack. GAME OVER ')
if lake.lower() == 'wait':
  print('It takes awhile but you safely make it across the lake')
  print('In front of you is a large house with 3 different colored doors.')
  print('One door is green, one blue, and one yellow. Which door will you open?')
  door = input('green, blue, yellow?')
elif lake.lower() == 'swim':
  print('Did you forget that you can\'t swim...GAME OVER')

if door.lower() == 'green':
  print('A man dashes out of the door with a sword.')
  print('He smiles at you and puts the sword down. he say\'s\n "Come in my friend we have been waiting for you. We will be heading out for a new adventure soon and will need you to come with us."')
  print('Rest well my friend you\'re safe...for now')
elif door.lower() =='blue':
  print('The room seems empty..you walk in...you hear a large smack on the back of your head and hit the ground')
  print('everything is fading to black. You\'re adventure is no more. GAME OVER')
elif door.lower() =='yellow':
  print('The room looks very peaceful.\n As you step in your hear a crashing sound.\n The floor is coloapsing, and now you\'re falling')
  print('You\'re still falling....still falling')
  print('Yup still have not hit the gound yet...this is not going to be good')
  print('Well you\'re still falling but I\'m getting tired of typing')
  print('So lets just save both of us time GAME OVER')
