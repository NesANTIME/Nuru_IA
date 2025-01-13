import subprocess
import os

def clear():
    os.system("cls")

def verificator():
    try:
        import speech_recognition as sr
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
    print("[+] by NesAnTime - NuruAI V1.0\n")

Logo()
if verificator() == False:
    subprocess.run(['python', 'Scripts/Update.py'])
else:
    subprocess.run(['python', 'Scripts/Nuru-IA.py'])