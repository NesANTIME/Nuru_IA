import os
import time
import json
import sys
import speech_recognition as sr
import pyttsx3
import unicodedata
from colorama import Fore, Style, init

init(autoreset=True)
engine = pyttsx3.init()
engine.setProperty('rate', 180) 
engine.setProperty('volume', 0.9)

def volmu(texto):
    print(f"\n {Style.BRIGHT}NURU-IA: {Style.NORMAL}")
    printt("      " + texto)
    engine.say(texto)
    engine.runAndWait()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def LectorUNDISK(name):
    try:
        with open(name, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            return json.loads(contenido)
    except FileNotFoundError:
        print("NURU-BD: No se encontró el archivo.")
    except json.JSONDecodeError:
        print("NURU-BD: El archivo no tiene el formato correcto.")
    return {}

def printt(text, delay=0.02):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def eliminar_tildes(texto):
    texto_sin_tildes = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    return texto_sin_tildes.strip()

def converter_textAaudi():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            print(f"\n {Style.BRIGHT}NURU-IA: {Style.NORMAL}")
            printt("      ¡Cuentame! Te Escucho.")

            try:
                audio = recognizer.listen(source)
                print(Fore.GREEN + Style.DIM + "\n [!] Procesando...")
                
                texto = recognizer.recognize_google(audio, language="es-ES")
                texto_procesado = eliminar_tildes(texto)
                return f"{texto_procesado}"
                
            except sr.UnknownValueError:
                return "No entendí lo que dijiste. ¿Puedes repetirlo?"
            except sr.RequestError as e:
                return f"Error al conectar con el servicio de reconocimiento de voz: {e}"
    except OSError:
        return "Error: No se encontró un micrófono disponible."

def ModeRestart():
    ModuloA = LectorUNDISK(os.path.join('Scripts/ModulosPreEntrenados/', 'ModuloA.json'))
    if not ModuloA:
        print("Error: No se encontró el módulo de respuestas. Verifica el archivo ModuloA.json.")
    return ModuloA

def Logo():
    clear()
    print(Style.BRIGHT + "███╗   ██╗██╗   ██╗██████╗ ██╗   ██╗      ██╗ █████╗ ")
    print(Style.BRIGHT + "████╗  ██║██║   ██║██╔══██╗██║   ██║      ██║██╔══██╗")
    print(Style.BRIGHT + "██╔██╗ ██║██║   ██║██████╔╝██║   ██║█████╗██║███████║")
    print(Style.BRIGHT + "██║╚██╗██║██║   ██║██╔══██╗██║   ██║╚════╝██║██╔══██║")
    print(Style.BRIGHT + "██║ ╚████║╚██████╔╝██║  ██║╚██████╔╝      ██║██║  ██║")
    print(Style.BRIGHT + "╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝       ╚═╝╚═╝  ╚═╝")
    printt("        [+] by NesAnTime - NuruAI V1.8 [+]\n")

def nucleo_ia_nuru():
    respuestas = ModeRestart()
    
    if not respuestas:
        print("Error: No hay respuestas cargadas en la IA. Saliendo del programa.")
        return
    
    while True:
        pregunta = converter_textAaudi()
        print(f"\n {Style.BRIGHT}Tú: { Style.NORMAL}\n      {pregunta}")
        
        if pregunta.lower() == "adios":
            volmu("¡Adiós! Fue un gusto ayudarte.")
            break
        else:
            respuesta = respuestas.get(pregunta.lower(), "Lo siento, no entiendo esa pregunta. Intenta aclararla.")
            volmu(respuesta)

nucleo_ia_nuru()
