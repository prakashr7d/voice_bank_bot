import speech_recognition as sr


r = sr.Recognizer()
file = sr.AudioFile('test.wav')

with file as source:
    audio = r.record(source)

try:
    recog = r.recognize_google_cloud(audio, language='en-US')
    print("You said: " + recog)
except sr.UnknownValueError as u:
    print(u)
    print("Google Cloud Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech Recognition service; {0}".format(e))
