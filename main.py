#TODO: Create a letter using starting_letter.txt
with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as mail:
    content = mail.read()

#for each name in invited_names.txt
with open("../Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as name:
    invite_name = name.readlines()

for item in invite_name:
    strip_item = item.strip()
    new_content = content.replace("[name]", strip_item)

    with open(f"Output/ReadyToSend/letter_for_{strip_item}.txt",mode="w") as new_file:
        new_file.write(new_content)

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp