#will find emails either in a word doc or in a text file

#import docx
import re
import pyperclip


Confirmation = input("ctrl + A to copy the entire document to your clipboard, and type ok and enter here when you have completed it \n")

#This is for telling it a file, but that doesnt work right now becuase there is no good way
#convert word doc to text to get it to work with isPhoneNumber
#inputfile = input("What is the full path of the document you want to extract from")

#inputfile = input("Copy and paste the whole text here; don't worry about how long it is. \n")


if Confirmation == "ok" or "Ok":
#Used for finding email
    emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

    text = str(pyperclip.paste())
    matches = []
    for groups in emailRegex.findall(text):
        Emull = matches.append(groups[0])
    #print(emailRegex)#For trying to gifgure out what it does.
    


    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('copied to clipboard:')
        print('\n'.join(matches))

    else:
        print('No phone numbers or email addresses found.')




#Here's crap that might be usable

##def getText(filename):
##    doc = docx.Document(filename)
##    fullText = []
##    for para in doc.paragraphs:
##        fullText.append(para.text)
##    return '\n'.join(fullText)
##
##result = getText(inputfile)
##print(result)

#doc = docx.Document(inputfile)

#for converting to text
#doctxt = doc2text.Document(inputfile)

#if zequestion == email

#just for testing purposes; should probably take it out later.     
#print(inputfile)

##for sentence in doc.paragraphs:
##    print(sentence.text)
