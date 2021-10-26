# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from constants import NEWYORK


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_check_new_york"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        state: Text = tracker.get_slot("GPE")
        print(state)
        dispatcher.utter_message(state)
        if state.lower() in NEWYORK:
            dispatcher.utter_message("not-qualified.mp3")
        else:
            dispatcher.utter_message(template="utter_transfer")

        return []
