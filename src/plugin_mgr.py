
from plugins import bash_this as bash

class razer:
    try:
        def change_color(hex_color):
            from plugins import razer_plug as razerPlug

            razerPlug.PLUGchange_color(hex_color)
            pass
    
        def Rainbow_road(facing=1):
            from plugins import razer_plug as razerPlug

            razerPlug.PLUGRainbow_road(facing)
            pass

    except Exception as e:
        print("error importing razer_plug.py")
        print()
        print(e)
        print()
        pass

class bash:
    try:
        def bash_this(command):
            from plugins import bash_this as bashPlug
            bashPlug.bash_this(command)
            pass

    except Exception as e:
        print("error importing bash_this.py")
        print()
        print(e)
        print()
        pass