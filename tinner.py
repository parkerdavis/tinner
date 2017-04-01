# Libraries that make this possible: #

import pickle
import random
import string

# various arrays to be used #

calledBack = 10
username = ""
password = ""

# uses chooseAuthMethod to originally log in. #

def login():   
    if input("\nUsername: ") == username:
        if input("\nPassword: ") == password:
            return True
            print("\nSuccess")
        else:
            print("\n============\n Try again:\n============ ")
            return False
    else:
        print("\n=================\n User not found:\n=================")
        return False
# Tweet class for defining what is in each composition. #

class Tweet():
    def __init__(self, content, hashtag, username):
        self.content = content
        self.hashtag = hashtag
        self.username = username
    def __str__(self):
        return self.username + "-" + self.content

def loadTweets():
    return pickle.load(open("tweets.p", "rb"))

# authMethod for original authentication of unique user. #

def chooseAuthMethod():
    c = input("\nSelection? \n 1: Login \n 2: Sign Up \n 3: Exit \nChoice: ")

    if c == 1 or "Login":
        return login()
    elif c == 2 or "Sign Up":
        print("\n Sign up here: ")
    elif c == 3 or "Exit" :
        print("\n Goodbye.")
    else:
        print("\n Not recognized. Try again.")

# loop for choosing action #

def loop():
    c = input("\nSelection? \n 1: Tweet \n 2: Go to feed \n 3: Logout \nChoice: ")

    if c == 1:
        CLC()
    elif c == 2:
        feed()
    elif c == 3:
        print("\n Goodbye.")
    else:
        print("\n Not recognized. Try again.")

# CLC = Command Line Compose. Function to allow original tweets to be composed according to usr. #

def CLC():
    comp = str(input("What are you thinking? \n Message: "))
    pickle.dump(Tweet(comp, "#thisistinner", "@highsmithdavis",), open("tweets.p", "ab"))

def feed():
    for tweet in PickleFunction():
        print(tweet)

def PickleFunction():
    with open("tweets.p") as f:
        unpickled = []
        while True:
            try:
                unpickled.append(str(pickle.load(f)))
            except EOFError:
                break
        return unpickled

# loggedIn = False
# while not loggedIn:
#     loggedIn = chooseAuthMethod()

while True:
    loop()

