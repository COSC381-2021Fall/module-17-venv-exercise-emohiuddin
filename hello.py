import pyjokes
import pyshorteners
import emoji

print("1. Get a pyjoke\n2.View an emoji\n3.Shorten a url\n")

loop=1

while(loop!=0):
    option=input("Please select an option : ")
    option=int(option)

    if (option==1):
        print(pyjokes.get_joke())

    if (option==2):
        word=input("Enter the word for emoji you want to see : ")
        word=str(word)
        print(emoji.emojize('Python is :'+word+':', use_aliases=True))

    if (option==3):
        url = input("Enter the url:")
        s = pyshorteners.Shortener()
        shortenurl = s.tinyurl.short(url)
        print(shortenurl)
    
    inp=input("\nContinue? True(1) or False(0) : ")
    loop=int(inp)
