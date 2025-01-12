import os
import time
import json
import sys
import subprocess
from colorama import Fore, Style, init
init(autoreset=True)

#Nivel Sistema
def clear():
    os.system("cls")

def verificator():
    try:
        import speech_recognition as sr
        return True
    except ImportError:
        return False
    
def modo_natural():
    subprocess.run(['python', 'Scripts/Lupt.py'])

def printt(text, delay=0.02):
    for letra in text:
        sys.stdout.write(letra)
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
    respuestas = {
        "hola": "¡Hola! ¿Cómo puedo ayudarte?",
        "que haces": "Ya sabes, Ajustando mi base de datos para tu próxima pregunta.",
        "como estas": "Estoy bien, gracias. ¿Y tú?",
        "que sabes": "Sé muchas cosas, pero no más allá de lo que esté en mi base de datos.",
        "que eres": "Soy una inteligencia artificial Creada Por NesAnTime. Creada para responder preguntas de tu vida diaria.",
        "cual es tu proposito": "Responder a tus preguntas y ayudarte con cosas básicas.",
        "quien te creo": "Fui creado Por NesANTIME, un programador con gran ambición por mejorarme."
    }
    return respuestas

def Logo():
    clear()
    printt("███╗   ██╗██╗   ██╗██████╗ ██╗   ██╗      ██╗ █████╗ ", 0.001)
    printt("████╗  ██║██║   ██║██╔══██╗██║   ██║      ██║██╔══██╗", 0.001)
    printt("██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗██║███████║", 0.001)
    printt("██║╚██╗██║██║   ██║██╔══██╗██║   ██║╚════╝██║██╔══██║", 0.001)
    printt("██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝      ██║██║  ██║", 0.001)
    printt("╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝       ╚═╝╚═╝  ╚═╝\n", 0.001)

def nucleo_ia_nuru():
    Logo()
    print("Recargando Modulos...")

    printt("¡Hola! Soy NURU-IA. Puedo Ayudarte en lo que necesites.")

    respuestas = ModeRestart()

    while True:
        pregunta = input(f"\n {Style.BRIGHT}Tú: {Style.NORMAL}\n    ").lower()

        if pregunta == "adios":
            printt("NURU-IA: ¡Adiós! Fue un gusto ayudarte.")
            break

        elif pregunta == "modo developers":
            print("Cargando... Modo Developer.")
            time.sleep(1)
            Logo()
            rut = input("Cargue el Archivo de Acceso a Memoria: ")
            nuevas_respuestas = LectorUNDISK(rut)
            chargate(20)
            if nuevas_respuestas:
                respuestas.update(nuevas_respuestas)
                time.sleep(3)
                print(f"NURU-BD: Acceso a Memoria ({rut}) Cargado exitosamente.")
                time.sleep(3)
            else:
                print("NURU-BD: No pude cargar el acceso a memoria.")

        elif pregunta == "desactivar modo developers":
            time.sleep(3)
            respuestas = ModeRestart()
            print(f"NURU-BD: Acceso a Memoria ({rut}) Eliminado exitosamente.")
            time.sleep(3)

        elif pregunta == "modo natural":
            if verificator() == True:
                print(Fore.GREEN + "     [+] Dependencias Instaladas Correctamente! ")
                time.sleep(2)
                modo_natural()  
            else:
                print(Fore.RED + "     [X] Dependencias NO Instaladas! ")
                print(Fore.WHITE + Style.DIM + "     -- por favor instala libreria pip install SpeechRecognition, pyaudio de python, Puedes Usar el comando: [pip install SpeechRecognition] Y [pip install pyaudio]")

        else:
            respuesta = respuestas.get(pregunta, "Lo siento, esa pregunta se escapa de mi entendimiento. o intenta cargar un modulo.")
            print(f"\n {Style.BRIGHT}NURU-IA: {Style.NORMAL}")
            printt("     " + respuesta)

nucleo_ia_nuru()
