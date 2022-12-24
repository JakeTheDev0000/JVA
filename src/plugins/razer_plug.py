import os 
import time

# change color of the keyboard to be a static color 
# DONT ADD THE # TO THE HEX COLOR
def PLUGchange_color(hex_color):
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