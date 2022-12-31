import os 
import time

# change color of the keyboard to be a static color 
# DONT ADD THE # TO THE HEX COLOR
def PLUGchange_color(hex_color="000000"):
    command = "polychromatic-cli -d keyboard -o static -c " + hex_color
    print(command)
    os.system(command)
    time.sleep(0.4)
    os.system(command)

# change color of the keyboard to be rainbow going 1: right and 2: left
def PLUGRainbow_road(facing=1):
    command = "polychromatic-cli -d keyboard -o wave -p {0}".format(facing)
    print(command)
    os.system(command)
    os.system(command)

def PLUGChange_Brightness(brightness=100):
    command = "polychromatic-cli -d keyboard -o brightness -p {0}".format(brightness)
    print(command)
    os.system(command)

def PLUGRecording_mode_effect():
    try:
        command = "polychromatic-cli -e rec"
        print(command)

        os.system(command)
    except:
        print("NO WAY TO PLAY EFFECT rec")

def PLUGNormal_mode_effect():
    try:
        command = "polychromatic-cli -e returnNORMAL"
        print(command)

        os.system(command)
    except:
        print("NO WAY TO PLAY EFFECT normal")

def PLUGError_effect():
    try:
        command = "polychromatic-cli -e error"
        print(command)

        os.system(command)
    except:
        print("NO WAY TO PLAY EFFECT error")

def PLUGstartup_jva_effect():
    try:
        command = "polychromatic-cli -e startupJVA"
        print(command)

        os.system(command)
    except:
        print("NO WAY TO PLAY startupJVA")