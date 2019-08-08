print("Enter '0' for exit.");
character = input("Enter any character: ");
if character == '0':
    exit();
else:
    if((character>='a' and character<='z') or (character>='A' and character<='Z')):
    	print(character, "is an alphabet.");
    else:
    	print(character, "is not an alphabet.");
