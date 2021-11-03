import pyjokes
import pyshorteners
from PyDictionary import PyDictionary


print("1. Get a pyjoke\n2.Find the meaning of a word from the dictionary\n3.Shorten a url\n")

loop=True

while(loop):
    option=input("Please select an option : ")
    option=int(option)

    if (option==1):
        print(pyjokes.get_joke())

    if (option==2):
        word=input("Enter the word : ")
        word=str(word)
        print(dictionary.meaning(word))

    if(option==3):
        url = input("Enter the url:")
        s = pyshorteners.Shortener()
        shortenurl = s.tinyurl.short(url)
        print(shortenurl)
    
    inp=input("Continue? True or False : ")
    loop=inp
