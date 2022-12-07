import os
import time
import random
from gtts import gTTS as gtts
from playsound import playsound as play
import speech_recognition as sr

import listOf as lof
def clear():
    return
    if os.name == 'nt':
        os.system('cls')
    if os.name == 'posix':
        os.system('clear')
    else:
        print("os not supported")
        print("edit JVA.py and add your os to the if statement in the clear function")
        exit()



def speak(text):
    lang = "en"
  
    myobj = gtts(text=text, lang=lang, slow=False)
    myobj.save("temp.mp3")
    play("temp.mp3")
    os.system("rm temp.mp3")

#  cant wait to refactor this later :D
def reconize_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        clear()
        print("Speak anything")
        # speak("Speak anything")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("you said : {}".format(text))
        speak("you said : {}".format(text))

        #! ASKING IF THATS WHAT YOU SAID
        clear()
        speak("is that what you said?")
        try:
            rb = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening... rb")
                audio = rb.listen(source)
                textb = rb.recognize_google(audio)
            
            if textb == "yes":
                print("yes")
                return text
            elif textb == "no":
                print("no")
                speak("re listening...")
                reconize_speech()
            else:
                print("Sorry could not recognize what you said")
                speak("You said: " + textb + " Sorry could not recognize what you said, please try again, i only reconize yes or no")
                reconize_speech()
        except:
            print("Sorry could not recognize what you said")
            speak("Sorry could not recognize what you said, please try again")
            reconize_speech()
        #! END ASKING IF THATS WHAT YOU SAID
    except:
        print("Sorry could not recognize what you said")
        speak("Sorry could not recognize what you said, please try again")
        reconize_speech()
    pass


def main():
    time.sleep(0.1)
    clear()

    print("Hello, I am JVA, your personal assistant.")
    while True:
        what_said = reconize_speech()
        try:
            print("what_said: " + what_said)
        except:
            print("what_said: {ERR2} what_said")


        for i in lof.list_of_clear:
            if what_said == i:
                clear()
                break
        for i in lof.list_of_exit:
            if what_said == i:
                speak("adios, amigo!")
                exit()
                break
        for i in lof.list_of_hello:
            if what_said == i:
                a = random.choice(list(lof.list_of_hello_response))
                print(a)
                speak(a)
                break
        for i in lof.list_of_hows_it_going:
            if what_said == i:
                a = random.choice(list(lof.list_of_hows_it_going_response))
                print(a)
                speak(a)
                break
        for i in lof.list_of_what_is_your_name:
            if what_said == i:
                a = random.choice(list(lof.list_of_what_is_your_name_response))
                print(a)
                speak(a)
                break
        
    pass

if __name__ == '__main__':
    print('JVA.py is being run directly')
    print("checking os...")
    print(os.name)
    print("os checked")
    print("starting main...")
    main()
