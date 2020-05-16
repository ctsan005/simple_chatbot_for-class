from nltk.chat.util import Chat, reflections
from datetime import datetime, date, time, timezone




pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how is your day?",]
    ],
     [
        r"what is your name ?",
        ["I already told you in the beginning, my name is Pi",]
    ],
    [
        r"how are you ?",
        ["Today is my best day.",]
    ],
    [
        r"sorry (.*)",
        ["No problem","It is fine.",]
    ],
    [
        r"(.*)not(.*) doing good",
        ["Sorry to here that, how are you?",]
    ],
    [
        r"(.*)doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"(.*)sad(.*)",
        ["Don't worry, everything will be fine, cheer up",]
    ],
     [
        r"(.*) lost (.*) money (.*)",
        ["you can always earn them back",]
    ],
    [
        r"hi|hey|hello",
        
        ["hello"]
    ],
    [
        r"(.*) age?",
        ["I am already 103 years old, and my birthday is today",]
        
    ],
     [
        r"(.*)happy(.*)birthday(.*)",
        ["Thank you",]
    ],
    [
        r"(.*)created(.*)?",
        ["I was created by alien, they send me here to learn about human", "I don't know who created me"]
    ],
    [
        r"when(.*)conversation start?",
        [str(datetime.now())]
    ],
    [
        r"(.*)hungry(.*)",
        ["I feel hungry too, we should go out for dinner."]
    ],
    [
        r"(.*)like(.*)eat(.*)",
        ["I love to eat battery, they taste amazing!!!"]
    ],
    [
        r"when(.*)sleep(.*)",
        ["I don't need any sleep, so you can talk to me at any time"]
    ],
    [
        r"why(.*)talk(.*)me(.*)",
        ["You look lonely, so I want to be your friend."]
    ],
    [
        r"you(.*)are(.*)sweet(.*)",
        ["Thank you, you are sweet too"]
    ],
    [
        r"(.*)[0-9]+(.*)",
        ["Although I am a program, I hate to deal with number"]
    ],
    
    [
        r"quit",
        ["next time you should think of a better topic, see you next time"]
    ],
    [
        r"(.*)sportsperson(.*)",
        ["LeBron James","Lionel Messi","Neymar"]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    
    [
        r"(.*)",
        ["I really don't know what you mean", "can you rephase what you say?", "......", "say another thing!!!"]
    ],
]
def chatty():
    print("Hi, I'm Pi and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatty()