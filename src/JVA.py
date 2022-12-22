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


clarify_each_time = False

def speak(text):
    print("JVA: " + text)
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
        if clarify_each_time:
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
                
                if textb in lof.list_of_yes:
                    print("yes")
                    return text
                elif textb in lof.list_of_no:
                    print("no")
                    speak("re listening...")
                    reconize_speech()
                else:
                    print("Sorry could not recognize what you said")
                    speak("You said: " + textb + " Sorry could not recognize what you said, please try again")
                    reconize_speech()
            except:
                print("Sorry could not recognize what you said")
                speak("Sorry could not recognize what you said, please try again")
                reconize_speech()
            #! END ASKING IF THATS WHAT YOU SAID
        else:
            return text
    except:
        print("Sorry could not recognize what you said")
        speak("Sorry could not recognize what you said, please try again")
        reconize_speech()
    pass


def main():
    time.sleep(0.1)
    clear()

    understand_what_user_said = False

    print("Hello, I am JVA, your personal assistant.")
    while True:
        understand_what_user_said = False
        what_said = reconize_speech()
        try:
            print("what_said: " + what_said)
        except Exception as e:
            print("what_said: {ERR2} what_said")
            print()
            print(e)
            print()

        if what_said in lof.list_of_exit:
            print("exit")
            speak("exiting, laters")
            print("exited at: " + time.strftime("%H:%M:%S", time.localtime()))
            exit()

        if what_said in lof.list_of_hello:
            print("hello")
            speak(lof.list_of_hello_response[random.randint(0, len(lof.list_of_hello_response) - 1)])
            understand_what_user_said = True
            pass
        elif what_said in lof.list_of_hows_it_going:
            print("how are you")
            speak(lof.list_of_hows_it_going_response[random.randint(0, len(lof.list_of_hows_it_going_response) - 1)])
            understand_what_user_said = True
            pass
        elif what_said in lof.list_of_what_is_your_name:
            print("what is your name")
            speak(lof.list_of_what_is_your_name_response[random.randint(0, len(lof.list_of_what_is_your_name_response) - 1)])
            understand_what_user_said = True
            pass

        if understand_what_user_said == False:
            print("did not understand what you said")
            speak("I did not understand what you said, please try again")
            pass

        time.sleep(1)
        pass
    pass

def test():
    print("test")
    import nltk

    # Get the user's input
    user_input = input("Enter your English input: ")

    # Tokenize the input
    tokens = nltk.word_tokenize(user_input)

    # Tag the tokens with their part-of-speech
    tags = nltk.pos_tag(tokens)

    # Print the tagged tokens
    print(tags)


    exit()
    pass
if __name__ == '__main__':
    print('JVA.py is being run directly')
    print("checking os...")
    print(os.name)
    print("os checked")
    print("starting main...")
    main()


