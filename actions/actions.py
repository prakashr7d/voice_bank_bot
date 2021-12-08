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
import logging


class ActionCheckAge(Action):

    def name(self) -> Text:
        return "action_check_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        age = tracker.get_slot("number")
        if age:
            if age > 64:
                dispatcher.utter_message(template="utter_type_of_medicare")
            else:
                dispatcher.utter_message(template="utter_not_qualified")
        else:
            dispatcher.utter_message(template="utter_age")
