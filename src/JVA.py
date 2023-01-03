# MAIN FILE FOR JVA
# MADE BY JAKE (MESSYCODE)
# COPYRIGHT (c) 2023
# MIT 

import sys
import os
import time
import random
from gtts import gTTS as gtts
from playsound import playsound as play
import speech_recognition as sr

#! list of sayings
import listOf as lof

#! PLUGINS
import plugin_mgr as plugmgr

args = sys.argv

wait_for_keyboard_animations = True
keyboard_animations = True

# Argument Manager \/
for arg in args:
    arg = str(arg)
    if arg.startswith("-pkd."):
        value = str(arg.replace("-pkd.", ""))
        value.lower()            
        if value == "true":
            wait_for_keyboard_animations = False
        elif value == "false":
            wait_for_keyboard_animations = True
        else:
            print("not a valid answer")
            exit(14)
    if arg.startswith("-nka"):
        value = str(arg.replace("-nka.", ""))
        value.lower()
        if value == "true":
            keyboard_animations = False
        elif value == "false":
            keyboard_animations = True
        else:
            print("not a valid answer")
            exit(14)
    if arg.startswith("--help") or arg.startswith("-h"):
        print("===================HELP===================")
        print("to enter the parm add (.), example: -pkd.true or -pkd.false")
        print("--help; -h : Brings up this screen")
        print("-pkd       : Pass Keyboard Delay, Wont wait for animations")
        print("-nka       : No Keyboard Animations")
        exit()



if keyboard_animations == True:
    plugmgr.razer.startup_jva()
if wait_for_keyboard_animations == True:
    time.sleep(1.5)




def clear():
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
    if keyboard_animations == True:
        plugmgr.razer.rec_mode()
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, 1)
        clear()
        print("Speak anything")
        # speak("Speak anything")
        audio_obj = r.listen(source)
        print(audio_obj)

    try:
        print("reconizing...")
        query = r.recognize_google(audio_obj)
        print("you said : {}".format(query))
        if clarify_each_time:
            speak("you said : {}".format(query))

            #! ASKING IF THATS WHAT YOU SAID
            clear()
            speak("is that what you said?")
            try:
                rb = sr.Recognizer()
                with sr.Microphone() as source:
                    print("listening... rb")
                    audio_obj = rb.listen(source)
                    textb = rb.recognize_google(audio_obj)
                
                if textb in lof.list_of_yes:
                    print("yes")
                    return query
                elif textb in lof.list_of_no:
                    print("no")
                    speak("re listening...")
                    reconize_speech()
                else:
                    print("Sorry could not recognize what you said")
                    speak("You said: " + textb + " Sorry could not recognize what you said, please try again")
                    reconize_speech()
            except:
                if keyboard_animations == True:
                    plugmgr.razer.error_mode()
                print("Sorry could not recognize what you said")
                speak("Sorry could not recognize what you said, please try again")
                reconize_speech()
            #! END ASKING IF THATS WHAT YOU SAID
        else:
            print(f"ITS {query}")
            return query
    except sr.UnknownValueError:
        if keyboard_animations == True:
            plugmgr.razer.error_mode()
        print("Sorry could not recognize what you said")
        speak("Sorry could not recognize what you said, please try again. RS-func")
        reconize_speech()
    except sr.RequestError:
        speak("Make Sure that you have a good Internet connection")
    except Exception as e:
        print(e)
        print("goodluck....")
        exit(1)
    pass


def main():
    time.sleep(0.1)
    clear()

    understand_what_user_said = False

    print("Hello, I am JVA, your personal assistant.")
    while True:
        understand_what_user_said = False
        what_said = str(reconize_speech())
        if keyboard_animations == True:
            plugmgr.razer.normal_mode()
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

        #! PLUGINS 
        # I know i could have just use LOF for bash_this... but for some ever reason that just wont work
        if what_said.startswith("command send ") or what_said.startswith("command sand") or what_said.startswith("commands sand"):
            print("command send")
            speak("sending command")
            plugmgr.bash.bash_this(what_said)
            understand_what_user_said = True
            pass

        if what_said in lof.chuck_norris_joke:
            speak(plugmgr.chuck_norris.get_joke())
            understand_what_user_said = True

        #! END PLUGINS
        if understand_what_user_said == False:
            if keyboard_animations == True:
                plugmgr.razer.error_mode()
            print("did not understand what you said")
            speak("I did not understand what you said, please try again")
            pass

        time.sleep(1)
        pass
    pass

def test():
    print("test")

    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

    exit()
if __name__ == '__main__':
    # test()
    print('JVA.py is being run directly')
    print("checking os...")
    print(os.name)
    print("os checked")
    print("starting main...")
    main()


