import speech_recognition as sr
import pyttsx3
import pywhatkit

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
            rec = listener.recognize_google(pc)
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
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        talk("Reproduciendo música" + music)
        print("Reproduciendo música " + music)
        talk("Reproduciendo música " + music)
        pywhatkit.playonyt(music)


if __name__ == "__main__":
    run_pepa()




