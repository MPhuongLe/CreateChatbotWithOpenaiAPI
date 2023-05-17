import pyttsx3

#Text to speech initialize
engine = pyttsx3.init() # object creation
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 200)     # setting up new voice rate
voices = engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id) 

def txt2speech(message):
    engine.say(message)
    engine.runAndWait()
    engine.stop()