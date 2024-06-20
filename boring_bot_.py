import time
import json  
import requests
from datetime import datetime

api_url = "https://bored-api.appbrewery.com/random"


bored_words = ["boring","bored","bore","boredom"]
time_words = ['time']
thank_words = ["thanks","thank"]
greet_words = ["hi","hey","hola","hello"]
bye_words = ["bye","tata","goodbye","allahhafiz"]
bad_words = ["pocha","nigga","bloody","damn","jerk","idiot","bastard","bullshit"
            ,"dammit","damn it" ,"damned","hell","shit","nigra"]






def listen():
    return input(">>>>>> ")




def decide(command):
    broken_words = command.split(" ")
    for word in broken_words:

        if word.lower() in bored_words:
            talkback("bored")
        elif word.lower() in time_words:
            talkback("time")
        elif word.lower() in thank_words:
            talkback("thank")
        elif word.lower() in greet_words:
            talkback("hello")
        elif word.lower() in bye_words:
            talkback("bye")
            return "bye"
        elif word.lower() in bad_words:
            talkback("bad")
        
    
    
    
            




def talkback(command):

    if(command=='bored'):
        response = requests.get(api_url)
        content2 = response.content.decode("UTF-8")
        dict_content = json.loads(content2)
        activity_ = dict_content["activity"]
        print(activity_)


    elif command=='time':
        c = datetime.now()
        current_time = c.strftime("%I:%M%p")
        print(f"It is {current_time}")


    elif command == "thank":
        print("You're welcome!")


    elif command == "hello":
        print("Hi Man")

    elif command == "bye":
        print("Bye, talk to you later")
        return "bye"
    
    elif command=="bad":
        print("you are suspended for 5 minutes")
        time.sleep(300)

    else:
        print("Couldn't detect anything from the word")






while True: 
    command = listen()
    res = decide(command)


    if res =="bye":
        break
    


