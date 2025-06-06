import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, keyboard,datetime
from pygame import mixer

name = "pepa"
listener = sr.Recognizer()
engine = pyttsx3.init()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  


def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    rec = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language='es-ES')
            rec = rec.lower()
            if name in rec: 
                rec = rec.replace(name, "")
    except sr.UnknownValueError:
        print("No se entendió el audio.")
    except sr.RequestError:
        print("Error con el servicio de reconocimiento.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    return rec


def run_pepa():

    while True:
        rec = listen()
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            talk("Reproduciendo música" + music)
            print("Reproduciendo música " + music)
            talk("Reproduciendo música " + music)
            pywhatkit.playonyt(music)

        elif 'busca' in rec:
            busqueda = rec.replace('busca', '')
            wikipedia.set_lang("es")
            informacion = wikipedia.summary(busqueda, 2)
            print(busqueda + " " + informacion)
            talk(informacion)

        elif 'alarma' in rec:
            alarm_time = rec.replace('alarma', '').strip()
            talk("Alarma establecida para " + alarm_time)
            print("Alarma establecida para " + alarm_time)
            alarma_sonando = False
            while True:
                hora_actual = datetime.datetime.now().strftime("%H:%M")
                if hora_actual == alarm_time and not alarma_sonando:
                    talk("¡Alarma sonando!")
                    mixer.init()
                    mixer.music.load('despierta.mp3')
                    mixer.music.play()
                    alarma_sonando = True
                if alarma_sonando:
                    if keyboard.is_pressed('s'):
                        mixer.music.stop()
                        break


        








if __name__ == "__main__":
    run_pepa()




