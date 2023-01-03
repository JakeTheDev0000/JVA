# THIS IS THE PLUGIN-MANAGER, THIS CONTROLS THE PLUGINS 
# MADE BY JAKE (MESSYCODE)
# COPYRIGHT (c) 2023
# MIT 

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

        def change_brightness(brightness):
            from plugins.razer_plug import PLUGChange_Brightness 

            PLUGChange_Brightness(brightness)
            pass
        
        def rec_mode():
            from plugins.razer_plug import PLUGRecording_mode_effect

            PLUGRecording_mode_effect()
            pass

        def normal_mode():
            from plugins.razer_plug import PLUGNormal_mode_effect

            PLUGNormal_mode_effect()
            pass

        def error_mode():
            from plugins.razer_plug import PLUGError_effect

            PLUGError_effect()
            pass
        
        def startup_jva():
            from plugins.razer_plug import PLUGstartup_jva_effect

            PLUGstartup_jva_effect()
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

class chuck_norris:
    try:
        def get_joke():
            from plugins.chuck_norris_jokes import PLUGGet_joke

            return PLUGGet_joke()
    except Exception as e:
        print("error importing chuck_norris_jokes.py")
        print()
        print(e)
        print()
        pass