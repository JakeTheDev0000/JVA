import os

def bash_this(command):
    command = command.replace("command send ", "")
    command = command.replace("command sand ", "")
    command = command.replace("commands sand ", "")
    command = command.lower()
    os.system(command)