#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open('./Input/Names/invited_names.txt') as names:
    for name in names.readlines():
        name = name.rstrip()
        with open('./Input/Letters/starting_letter.txt') as letter:
            for line in letter:
                if '[name]' in line:
                    line = line.replace('[name]', name)
                    with open(f'./Output/ReadyToSend/{name}_invitation', mode='w') as invite:
                        invite.write(line)
                else:
                    with open(f'./Output/ReadyToSend/{name}_invitation', mode='a') as invite:
                        invite.write(line)



#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp