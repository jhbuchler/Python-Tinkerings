def isPhoneNumber(text):
    if len(text) != 12:
        return False # length not consistent with standard dashed phone num format
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != "-":
        return False # missing dash
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # issue with first 3 digits
    if text[7] != "-":
        return False # missing dash
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False # issue with last 4 digits
    return True


message = input("Please enter an emergency contact number: ")
foundNumber = False
for i in range(len(message)):
    segment = message[i:i+12]
    if isPhoneNumber(segment):
        print("Phone number found: " + segment)
        foundNumber = True
if not foundNumber:
    print("Please enter a valid 9-digit phone number (Exa. 555-555-5555)")

            
    
