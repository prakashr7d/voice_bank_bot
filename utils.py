from typing import Text

import soundfile as sf

import sounddevice as sd


def record_audio(default_file_name: Text):
    fs = 44100
    duration = 5
    sd.default.samplerate = fs
    sd.default.channels = 1
    myrecording = sd.rec(duration * fs)
    sd.wait()
    sf.write(default_file_name, myrecording, samplerate=fs, format="wav")
