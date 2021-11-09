import os
from typing import Text

from google.cloud import speech


class GoogleRecognise:
    def __init__(self, uri: Text):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'google_secret_key.json'
        self.client = speech.SpeechClient()
        self.uri = uri
        self.config = speech.RecognitionConfig(
            enable_automatic_punctuation=True,
            audio_channel_count=1,
            sample_rate_hertz=44100,
            language_code="en-US"
        )
        self.response = None

    def open_audio(self):
        audio = speech.RecognitionAudio(uri=self.uri)
        return audio

    def recognise(self):
        self.response = self.client.recognize(request={"config": self.config, "audio": self.open_audio()})

    def get_response(self):
        for result in self.response.results:
            return result.alternatives[0].transcript

# setting Google credential

# create client instance


# the path of your audio file


# Sends the request to google to transcribe the audio

# Reads the response

