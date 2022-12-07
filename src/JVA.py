import os
import time
import random
from gtts import gTTS as gtts
from playsound import playsound as play
import speech_recognition as sr

import listOf as lof
def clear():
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
        text_split = r.recognize_google(audio).split("listening...")

        text = r.recognize_google(audio)
        print("you said : {}".format(text_split[1]))
        speak("you said : {}".format(text_split[1]))

        # ask if thats what you said
        # if yes then return text_split[1]
        # if no then

        speak("is that what you said?")
        try:
            rb = sr.Recognizer()
            with sr.Microphone() as source:
                print("listening... rb")
                audio = rb.listen(source)
                textb = rb.recognize_google(audio)
            
            if textb == "yes":
                return text_split[1]
            else:
                reconize_speech()
        except:
            print("Sorry could not recognize what you said")
            speak("Sorry could not recognize what you said, please try again")
            reconize_speech()
    except:
        try:
            text = r.recognize_google(audio)
            print("you said : {}".format(text))
            speak("you said : {}".format(text))

            speak("is that what you said?")
            try:
                rb = sr.Recognizer()
                with sr.Microphone() as source:
                    print("listening... rb")
                    audio = rb.listen(source)
                    textb = rb.recognize_google(audio)
                
                if textb == "yes":
                    return text
                else:
                    reconize_speech()
            except:
                print("Sorry could not recognize what you said")
                speak("Sorry could not recognize what you said, please try again")
                reconize_speech()

        except:                
            print("Sorry could not recognize what you said")
            speak("Sorry could not recognize what you said")

            return "{ERR1}Sorry could not recognize what you said"
    pass


def main():
    time.sleep(0.1)
    clear()

    print("Hello, I am JVA, your personal assistant.")
    while True:
        what_said = reconize_speech()
        try:
            if what_said.split("{ERR1}")[0] == "":
                print("error")
        except:
            print("no error")
            pass
        # if what_said == "clear":
        #     clear()
        # if what_said == "exit":
        #     exit()
        # if what_said == "hello":
        #     print("hello")
        #     speak("hello")

        for i in lof.list_of_clear:
            if what_said == i:
                clear()
                break
        for i in lof.list_of_exit:
            if what_said == i:
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
