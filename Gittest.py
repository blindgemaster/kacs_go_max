import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    print('Lolo1: ', audio)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    speak('Hello sir I am Lolo 1')


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query1 = r.recognize_google(audio, language='en-in')
        print(query1)
    except:
        print('Say that again please')
        return 'None'
    return query1


if __name__ == '__main__':
    wishme()
    while True:
        query = input('User: ')
        if 'who is' in query:
            try:
                speak('Let me think sir')
                query = query.replace('who is', '')
                results = wikipedia.summary(query, sentences=1)
                speak('Yeah i know what you are refering to')
                speak(results)
            except:
                speak('I could not think of what you were reffering to')
        elif 'bye' in query:
            speak('Bye sir')
            break
        elif 'how are you' in query:
            speak('I am fine sir')
        elif 'name' in query:
            speak('Khizar')
        elif 'good' in query:
            speak('Thank you sir')
        elif 'ok' in query or 'okay' in query:
            speak('okay sir')
        else:
            speak("I couldn't understand sir")
