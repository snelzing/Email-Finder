
import re
import pyperclip


Confirmation = input("ctrl + A to copy the entire document to your clipboard, and type ok and enter here when you have completed it \n")



if Confirmation == "ok" or "Ok":
#Used for finding email
    emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []
    for groups in emailRegex.findall(text):
        Emull = matches.append(groups[0])

    


    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('copied to clipboard:')
        print('\n'.join(matches))

    else:
        print('No phone numbers or email addresses found.')




