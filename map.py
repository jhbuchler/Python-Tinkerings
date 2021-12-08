import webbrowser, sys, pyperclip

sys.argv # ['map', '1600', 'Pennsylvania', 'Ave', 'NW']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    # ['map', '1600', 'Pennsylvania', 'Ave', 'NW'] ---> '1600 Pennsylvania Ave NW'
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

#Requires .bat file and set PATH variable
