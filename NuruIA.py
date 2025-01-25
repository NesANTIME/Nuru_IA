import subprocess
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def verificator():
    try:
        import speech_recognition as sr
        import pyttsx3
        return True
    except ImportError:
        return False
    
def Logo():
    clear()
    print("███╗   ██╗██╗   ██╗██████╗ ██╗   ██╗      ██╗ █████╗ ")
    print("████╗  ██║██║   ██║██╔══██╗██║   ██║      ██║██╔══██╗")
    print("██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗██║███████║")
    print("██║╚██╗██║██║   ██║██╔══██╗██║   ██║╚════╝██║██╔══██║")
    print("██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝      ██║██║  ██║")
    print("╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝       ╚═╝╚═╝  ╚═╝")
    print("[+] by NesAnTime - NuruAI V1.7\n")

if verificator() == False:
    Logo()
    subprocess.run(['python', 'Scripts/Update/Update.py'])
else:
    subprocess.run(['python', 'Scripts/Nuru-IA.py'])