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

#    """Example of a custom form action"""
#
#    def name(self):
#        """Unique identifier of the form"""
#        return "greetName_form"

#    @staticmethod
#    def required_slots(tracker: Tracker) -> List[Text]:
#        """A list of required slots that the form has to fill"""

#        return ["name"]

#    def slot_mappings(self):
#        response = {
#            "name": [self.from_entity(
#                entity="name", intent=["inform_name"]
#                ),
#            ]
#        }
    #print(response)
#        return(response)

#    def submit(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: Dict[Text, Any],
#    ) -> List[Dict]:
#        """Define what the form has to do
#            after all required slots are filled"""

#        dispatcher.utter_template("utter_greet_name", tracker)
#        return []


#class ActionGreet(Action):
#    def name(self) -> Text:
#        return "action_greet"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#        name = tracker.get_slot("mood")

#        if mood == "None":


#        with open("mood_historic.txt", "a+") as file:
#            file.write(mood + '\n')

#    dispatcher.utter_template("utter_greet", tracker)


class ActionStoreMood(Action):
    def name(self) -> Text:
        return "action_store_mood"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        mood = tracker.get_slot("mood")

        with open("mood_historic.txt", "a+") as file:
            file.write(mood + '\n')

        #dispatcher.utter_message(text=f"Your mood '{mood}' have been recorded!")
        #return [SlotSet("mood_historic", mood)]


class ActionDebugBot(Action):
    def name(self) -> Text:
        return "action_debug_bot"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        dispatcher.utter_message(text="Debug away, captain!")


class DemographicForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        """Unique identifier of the form"""
        return "demographic_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return [
            "age",
            "gender",
            "neighborhood",
            "therapy",
            "ethnicity",
            "work",
            "major",
            "timeunb",
        ]

    def slot_mappings(self):
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        response = {
            "age": [
                self.from_entity(
                    entity="number", intent=["inform_number"]
                ),
            ],

            "gender": self.from_entity(entity="gender"),

            "neighborhood": self.from_entity(entity="neighborhood"),

            "therapy": [
            self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)
            ],

            "ethnicity": self.from_entity(entity="ethnicity"),

            "work": [
            self.from_intent(intent="affirm", value=True),
            self.from_intent(intent="deny", value=False)
            ],

            "major": self.from_entity(entity="major"),

            "timeunb": [
                self.from_entity(
                    entity="number", intent=["inform_number"]
                ),
            ],
        }
        #print(response)
        return(response)

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_template("utter_end_demographic", tracker)
        return []
