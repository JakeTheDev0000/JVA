# runs a bash command
# MADE BY JAKE (MESSYCODE)
# COPYRIGHT (c) 2023
# Apache License 2.0 

import os

def bash_this(command):
    command = command.replace("command send ", "")
    command = command.replace("command sand ", "")
    command = command.replace("commands sand ", "")
    command = command.lower()
    os.system(command)