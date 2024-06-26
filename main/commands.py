import keyboard
import webbrowser
import subprocess
import abc
import yaml

class VoiceCommand(abc):
   
   def __init__(text):
    with open("C:/Users/User/Desktop/PROG/.vscode/voice_helper/main/user_com.yml") as fh:
        read_data = yaml.load(fh, Loader=yaml.FullLoader)

        if read_data.count(text):




    class Сommands(VoiceCommand):
        
        def press_and_relase(hotkey):
            
            keyboard.press_and_release(hotkey)
        
            return()
        
        def browser_search(browser_path, browser_name, url):
            
            webbrowser.register(browser_name, None, webbrowser.BackgroundBrowser(browser_path))
            webbrowser.get(browser_name).open(url)
            
            return()

        def open_exefile(exe_path):
            
            subprocess.call([exe_path])
            
            return()
    