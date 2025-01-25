import os
import time
import json
import sys
import subprocess
import speech_recognition as sr
from colorama import Fore, Style, init
init(autoreset=True)

#Nivel Sistema
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def update():
    subprocess.run(['python', 'Scripts/Update/Update.py'])
    if os.path.exists(os.path.join('Scripts/', 'Update/NewUpdate.txt')):
        return True
    else:
        return False
    
def New_Update_create():
    with open(os.path.join('Scripts/', 'Update/NewUpdate.txt'), 'r') as archivo:
        text = archivo.read()
        return text

def printt(text, delay=0.02):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def chargate(total, duracion=2):
    for i in range(total + 1):
        porcentaje = int((i / total) * 100)
        barra = "#" * i + "-" * (total - i)
        sys.stdout.write(f"\r[{barra}] {porcentaje}%")
        sys.stdout.flush()
        time.sleep(duracion / total)
    print()

#Nivel AutoTotal
def LectorUNDISK(name):
    try:
        with open(name, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return json.loads(contenido)
    except FileNotFoundError:
        print("NURU-BD No se encontró el archivo. Asegúrate de que el nombre sea correcto.")
    except json.JSONDecodeError:
        print("NURU-BD: El archivo no tiene el formato correcto.")
    return {}

def ModeRestart():
    ModuloA = LectorUNDISK(os.path.join('Scripts/ModulosPreEntrenados/', 'ModuloA.json'))
    return ModuloA

def Logo():
    clear()
    print(Style.BRIGHT + "███╗   ██╗██╗   ██╗██████╗ ██╗   ██╗      ██╗ █████╗ ")
    print(Style.BRIGHT + "████╗  ██║██║   ██║██╔══██╗██║   ██║      ██║██╔══██╗")
    print(Style.BRIGHT + "██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗██║███████║")
    print(Style.BRIGHT + "██║╚██╗██║██║   ██║██╔══██╗██║   ██║╚════╝██║██╔══██║")
    print(Style.BRIGHT + "██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝      ██║██║  ██║")
    print(Style.BRIGHT + "╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝       ╚═╝╚═╝  ╚═╝")
    printt("        [+] by NesAnTime - NuruAI V2.0 [+]\n")

def nucleo_ia_nuru():
    Logo()
    
    if update() == True:
        printt("¡Hola! Soy NURU-IA. " + New_Update_create())
        print(f"{Style.BRIGHT}NURU-IA: {Style.NORMAL}Puedo Ayudarte en lo que necesites. ")
    else: 
        printt("¡Hola! Soy NURU-IA. Puedo Ayudarte en lo que necesites. ")  

    respuestas = ModeRestart()

    while True:
        pregunta = input(f"\n {Style.BRIGHT}Tú: {Style.NORMAL}\n    ").lower().strip()

        if pregunta == "adios":
            print(f"\n {Style.BRIGHT}NURU-IA: {Style.NORMAL}")
            printt("      ¡Adiós! Fue un gusto ayudarte.")
            break

        elif pregunta == "/cargar modulo":
            print(Fore.GREEN + "[!] Cargando...")
            time.sleep(1)
            Logo()
            rut = input(Fore.YELLOW + Style.DIM + " [+] Cargue la ruta del archivo de Acceso a Memoria: ")
            respuestas_up = LectorUNDISK(rut)
            chargate(20)
            if respuestas_up:
                respuestas.update(respuestas_up)
                time.sleep(3)
                print(Fore.GREEN + f"[!] NURU-BD: Acceso a Memoria ({Fore.WHITE + rut + Fore.GREEN}) Cargado exitosamente.")
                time.sleep(3)
            else:
                print(Fore.RED + "[!] NURU-BD: No pude cargar el acceso a memoria.")

        elif pregunta == "/eliminar modulos":
            time.sleep(3)
            respuestas = ModeRestart()
            print(Fore.GREEN + f"[!] NURU-BD: Acceso a Memoria ({Fore.WHITE + rut + Fore.GREEN}) Eliminado exitosamente.")
            time.sleep(3)

        elif pregunta == "/voz":
            subprocess.run(['python', 'Scripts/Nuru-IA-MIC.py'])
            
        else:
            respuesta = respuestas.get(pregunta, "Lo siento, esa pregunta se escapa de mi entendimiento. o intenta cargar un modulo.")
            print(f"\n {Style.BRIGHT}NURU-IA: {Style.NORMAL}")
            printt("     " + respuesta)


nucleo_ia_nuru()
