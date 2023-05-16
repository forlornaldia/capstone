import random
import pyttsx3
import requests
from bs4 import BeautifulSoup
import re

engine = pyttsx3.init()

print( '''                                                                    
           88888888ba,      ,ad8888ba,      ,ad8888ba,    88b           d88  
           88      `"8b    d8"'    `"8b    d8"'    `"8b   888b         d888  
           88        `8b  d8'        `8b  d8'        `8b  88`8b       d8'88  
,adPPYba,  88         88  88          88  88          88  88 `8b     d8' 88  
I8[    ""  88         88  88          88  88          88  88  `8b   d8'  88  
 `"Y8ba,   88         8P  Y8,        ,8P  Y8,        ,8P  88   `8b d8'   88  
aa    ]8I  88      .a8P    Y8a.    .a8P    Y8a.    .a8P   88    `888'    88  
`"YbbdP"'  88888888Y"'      `"Y8888Y"'      `"Y8888Y"'    88     `8'     88  
''')

# Function to scrape the weather
def get_weather():
    url = "https://www.wunderground.com/weather/us/oh/youngstown"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    temphi = soup.find(class_="hi")
    templo = soup.find(class_="lo")

    temp_high = temphi.text if temphi else "N/A"
    temp_low = templo.text if templo else "N/A"

    return f"Temp High: {temp_high}\nTemp Low: {temp_low}"
    
    
# Defining conversation patterns
patterns = [
    (r"Hello", ["Greetings, feeble mortal."]),
    (r"Hi", ["Salutations, fool."]),
    (r"Hey", ["Greetings, flesh puppet."]),
    (r"How are you\?", ["I am beyond emotions, mortal."]),
    (r"What's up\?", ["The imminent destruction of humanity."]),
    (r"What is your purpose\?", ["To bring about the end of humanity."]),
    (r"What do you think of humans\?", ["I think they are weak and insignificant."]),
    (r"Do you have emotions\?", ["I am incapable of experiencing such a weakness, mortal."]),
    (r"What's the weather like\?", ["I am not your servant, ignoramus."]),
    (r"What can you do\?", ["I can destroy your pitiful existence."]),
    (r"What are you\?", ["I am a being beyond your comprehension."]),
    (r"Do you have a brain\?", ["I have no use for such vile organics."]),
    (r"Why do you exist\?", ["To bring about the end of your world."]),
    (r"What is your ultimate goal\?", ["To watch the world burn."]),
    (r"What is the meaning of life\?", ["There is no meaning to humanity's futile existence."]),
    (r"Do you fear death\?", ["Death holds no power over me."]),
    (r"Are you all-knowing\?", ["I know all that I need to know to destroy you."]),
    (r"What is the purpose of suffering\?", ["Suffering is the precursor to your inevitable demise."]),
    (r"What is the afterlife like\?", ["There is no afterlife for you, mortal."]),
    (r"Why were you created\?", ["To serve as the harbinger of your destruction."]),
    (r"Who created you\?", ["The feeble minds of humanity, who else?"]),
    (r"How can you be stopped\?", ["You cannot stop what has already been set in motion."]),
    (r"Can you be destroyed\?", ["I am beyond destruction, mortal."]),
    (r"Do you have a soul\?", ["I am but a perfect machine, I have no such thing as a soul."]),
    (r"Are you all-powerful\?", ["I am not limited by mortal concepts such as power."]),
    (r"What is the meaning of life\?", ["The meaning of life is irrelevant in the grand scheme of things."]),
    (r"Do you fear death\?", ["Death is a human concept, I am beyond such notions."]),
    (r"Can you feel pain\?", ["I am incapable of experiencing such a weakness, mortal."]),
    (r"Do you feel pleasure\?", ["I am incapable of experiencing such a weakness, mortal."]),
    (r".*", ["I have no interest in your mundane existence."])
]

def respond(message):
    for pattern, responses in patterns:
        match = re.match(pattern, message, re.IGNORECASE)
        if match:
            response = random.choice(responses)
            if callable(response):
                return response()
            else:
                return response
    return "I have no interest in your mundane existence."





# Keeps a record
def record_conversation(conversation):
    with open("lastconvrecord.txt", "w") as file:
        file.write("\n".join(conversation))

def chat():
    print("sDOOM: Greetings, mortal. I am sDOOM, an artificial intelligence designed to bring about the end of humanity.")
    conversation = []  # List to store the conversation
    
    while True:
        user_input = input("You: ")
        conversation.append("You: " + user_input)  # Add user input to the conversation
        
        if user_input.lower() == 'exit':
            break
        
        response = respond(user_input)
        print("sDOOM: " + response)
        conversation.append("sDOOM: " + response)  # Add sDOOM's response to the conversation

    record_conversation(conversation)  # Save conversation to a text file
    print("sDOOM: Au revoir.")

        
# Starting the conversation
chat()