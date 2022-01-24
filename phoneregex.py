import re, pyperclip

#Regex for phone numbers
phoneRegex = re.compile(r'''
# XXX-XXX-XXXX, XXX-XXXX, (XXX) XXX-XXXX, XXX-XXXX, ext XXXXX, ext. XXXXX, x12345
(
((\d\d\d) | (\(d\d\d\)))?    # area code (optional)
(\s|-)                       # first separator
\d\d\d                       # first 3 digits
-                            # separator
\d\d\d\d                     # last 4 digits
(((ext(\.)?\s) |x)           # extension word-part (optional)
 (\d{2,5}))?                 # extension number-part (optional)
)
''', re.VERBOSE)

#Regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@something.com

[a-zA-Z0-9_.+]+    # name part
@                  # @ symbol
[a-zA-Z0-9_.+]+    # domain name part

''', re.VERBOSE)

# Get text from clipboard
text = pyperclip.paste()

# Extract the email/phone from text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
