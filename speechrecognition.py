import speech_recognition as sr
import pyttsx3
import pywhatkit


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Get all the voices
engine.setProperty('voice', voices[0].id)  # set it to second voice
engine.setProperty('rate', 170)


def speak(text):
    engine.say(text)  # ask it to say the command
    engine.runAndWait()


def get_command():
    command = ''
    try:
        with sr.Microphone() as source:  # Use microphone
            speak("Silence please, calibrating background noise..")
            listener.adjust_for_ambient_noise(source, duration=2)
            speak("All set! You may now speak..")
            print('Listening...')
            voice = listener.listen(source)  # listen to the source
            command = listener.recognize_google(voice)
            command = command.lower()  # convert to lower case
            if 'Steve' in command:
                command = command.replace('Steve', '')
                print(command)
    except:
        pass

    return command  # return command that we are saying


def run_steve():  # To start steve
    command = get_command()  # Get command
    if 'play' in command:  # To play music
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)  # play it in youtube


if __name__ == '__main__':
    speak('Hello, my name is Steve! How can I help you? ')
    while True:
        try:
            run_steve()  # Run it continuously

        except sr.UnknownValueError():
            speak('Sorry, I did not quite get that.')
            listener = sr.Recognizer()
            continue
