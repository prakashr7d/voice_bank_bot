FROM rasa/rasa-x:latest as base

RUN pip install pip==21.3.1

RUN pip install twilio

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
ADD constants.py constants.py
ADD twillio_voice_custom.py twillio_voice_custom.py
