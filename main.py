import sys
import threading
from random import randrange
import requests
import os
import time


URLChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
URLCharsLen = len(URLChars)


def getURL():
    generalStr = "http://i.imgur.com/"
    for i in range(6):
        generalStr+=URLChars[randrange(URLCharsLen)]
    generalStr +=".png"
    return generalStr

def getURL(postfix):
    generalStr = "http://i.imgur.com/" + postfix
    return generalStr

def getPostfix():
    generalStr = ""
    for i in range(6):
        generalStr+=URLChars[randrange(URLCharsLen)]
    generalStr +=".png"
    return generalStr

def makeThings(args):
    while(True):
        postfix = getPostfix()
        resourceUrl = getURL(postfix)
        try:
            content = requests.get(resourceUrl)
            try:
                check = content.history[1]
            except:
                if content.status_code != 429:
                    #print("OK")
                    try:
                        with open(args['storage'] + "\\" + postfix, "wb") as f:
                            f.write(content.content)
                            print("Got: " + postfix)
                    except:
                        print("Storage corupted")
                else:
                    print("Server throws Too Many Requests... Thread paused")
                    time.sleep(30)

        except:
            print("URL corupted: " + resourceUrl)

    pass














def main(args):
    threads = []
    for i in range(int(args['threads'])):
        thread = threading.Thread(target=makeThings, args=(args, ))
        threads.append(thread)
        thread.start()

    while(True):
        inpt = input("q to exit")
        if(inpt == "q" or inpt == "Q"):
            sys.exit()

    pass


def printHello(args):
    logo = "                                                            \n                                                            \n                                                            \n                     .-.                 .                  \n                    =%%%+.             .*%*                 \n                  .*%%%%%%-           -#%%%#.               \n                 =%%%%%%%%%= : :. :  =#%%%%%%.              \n               :#%%%%%%%%%%%-+:   :=#%%%%%%%%#.             \n              +%%%%%########+=  .-*****####%%%+             \n             *%%##***************************##             \n            +##********************************.            \n           .***********************************.            \n          . ************************************+=.         \n          :=-*************************************          \n         .--****************************++******=           \n           .:-**********************+=:...:****:            \n            .#%#*******++**********+-.....:***=:           \n            *%%%%%##****:.::--==--:.........:*#*:           \n           .%%%%%%%%%%%#=.....::....:.:=-:...=%%*           \n           :%%%%%%%%%%%%#:...:=+:.::--:--:...-#%%+          \n            #::%%%%%%%%%#-........::::.......:#%%%-         \n               .*%%%%%%%%=...................=%%%%+         \n                 =**%%%%%=..................:*%#%%#         \n                   .*%%%#-.......:.....:...---+: -#         \n                     .-#*::::::=%%%=-+%%#:.       .         \n                                %%%%*%%%+                   \n                                ==-. .-=:                   \n                                                            \n                                                            \n        \n"
    print(logo + "Welcomne to Alaster, the Imgur parser. \n You run on next parameters:\n" + args)
    pass


def test(args):
    postfix = "/lEUsq.png"
    content = requests.get(getURL(postfix))
    try:
        print(args['storage'] + "\\file.png")
        with open(args['storage'] + "\\file.png", "wb") as f:
            f.write(content.content)

    except IOError:
        print(IOError)


    while(True):
        pass

if __name__ == '__main__':

    args = {'threads': 10, 'isCustomStorage': False, 'storage': "root"}
    args['threads'] = sys.argv[1]
    args['isCustomStorage'] = sys.argv[2]
    if args['isCustomStorage'] == True or args['isCustomStorage'] == "True":
        args['storage'] = sys.argv[3]
        args['isCustomStorage'] = True
    else:
        args['storage'] = os.getcwd()
    paramString = ""

    for arg in args.keys():
        paramString += (arg + " : " + str(args[arg])) + "\n"

    #test(args)
    printHello(paramString)
    main(args)

