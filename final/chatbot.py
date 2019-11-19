import os
from nltk import word_tokenize
import enchant
from enchant import DictWithPWL
from enchant.checker import SpellChecker
import re
from datetime import datetime
import string
from profanity_check import predict, predict_prob #need to install profanity_check using pip3

def check():
    off_word=0
    file_content = open("res.json").read()
    #d = enchant.Dict("en_US")
    my_dict = DictWithPWL("en_US", "wordlist.txt")
    my_checker = SpellChecker(my_dict)
    #incor=list(set([word.encode('ascii', 'ignore') for word in word_tokenize(file_content) if d.check(word) is False and re.match('^[a-zA-Z ]*$',word)] ))
    incor=list(set([word.encode('ascii', 'ignore') for word in word_tokenize(file_content) if my_checker.check(word) is False and re.match('^[a-zA-Z ]*$',word)] ))
    for word in word_tokenize(file_content):
        i=predict([str(word)])
        if i==1:
            off_word=off_word+1
    print("\nANALYSIS REPORT OF URL\n")
    print("----------------------\n")
    len_list=len(incor)
    print(str(off_word)+" Offensive word(s) found !")
    print("Number of incorrect words : "+str(len_list))
    show=input("List incorrect words ?\n>>>")
    if show.lower()=="yes":
        print("\nIncorrect Words:\n")
        print(incor)
    else:
        pass
    os.remove("res.json")

print("---------------------------------------------")
print("|                 CHATBOT                   |")
print("---------------------------------------------")
while True:
    usr=input(">> ")
    qry=usr.lower()
    if "hello" in qry or "hi" in qry :
        print("Hi, how are you doing ? :)")
        reply=input(">>> ").lower()
        if "not good" in reply or  "bad" in reply:
            print("sorry to hear that")
        elif "good" in reply or  "fine" in reply:
            print("Happy to hear that")
        else:
            print("Sorry, I didn't get that")
    elif "bye" in qry or "exit" in qry or "quit" in qry:
        print("Bye bye,have a good day \n")
        exit()
    elif "time" in qry and ("day" in qry or "date" in qry):
        print("The time is "+str(datetime.now().time().strftime('%H:%M'))+" and today is "+str(datetime.now().date().strftime('%d-%m-%Y')))
    elif "time" in qry:
        print("The time is "+str(datetime.now().time().strftime('%H:%M')))
    elif "date" in qry or "day" in qry:
            print("Today's date is "+str(datetime.now().date().strftime('%d-%m-%Y')))
    elif "created" in qry or "creator" in qry or "mother" in qry or "father" in qry:
        print("A group of studemts from FISAT created me")
    elif "who are you" in qry or "what are you" in qry:
        print("I am a chatbot. I am here to help you.")
    elif "check" in qry or "url" in qry or "analyze" in qry or "find" in qry:
        print("Enter the url to the website you want to scrape")
        url=input(">>> ")
        f=open("url.txt","w")
        f.write(url)
        f.close()
        os.system('scrapy crawl finder -o res.json')#to run shell command.should delete output file aftet processing !!!!!
        os.remove('url.txt')
        check()
    else:
        print("Sorry, I didn't understand what you said")
    print("\n")
    
    