# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction

# class ActionFacilitySearch(Action):

#     def name(self) -> Text:
#         return "action_facility_search"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         facility = tracker.get_slot("facility")
#         address = "123 Quarantine Street"
#         dispatcher.utter_message(text="Sure, I'm on it!")
#         dispatcher.utter_message(text=f"The address is {address}")

#         return [SlotSet("address", address)]

class ActionDebugBot(Action):
    def name(self) -> Text:
        return "action_debug_bot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
            import ipdb; ipdb.set_trace()
            dispatcher.utter_message(text="Debug away, captain!")

class DemographicForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        """Unique identifier of the form"""
        return "demographic_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["age", "gender", "neighborhood", "therapy", "ethnicity",
        "work", "major", "timeunb"]

    def slot_mappings(self):
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        return {
        "age": self.from_entity(entity="age"),
        "gender": self.from_entity(entity="gender"),
        "neighborhood": self.from_entity(entity="neighborhood"),
        "therapy": self.from_entity(entity="therapy"),
        "ethnicity": self.from_entity(entity="ethnicity"),
        "work": self.from_entity(entity="work"),
        "major": self.from_entity(entity="major"),
        "timeunb": self.from_entity(entity="timeunb")
        }


    def submit(
    self,
    dispatcher: CollectingDispatcher,
    tracker: Tracker,
    domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_template('utter_end_demographic', tracker)
        return []
