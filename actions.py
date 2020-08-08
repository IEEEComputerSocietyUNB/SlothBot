# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from datetime import datetime
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
        user = tracker.slots.get("name", "no name")
        mood = tracker.get_slot("mood")
        timestamp = datetime.fromtimestamp(tracker.events[-1]['timestamp'])
        timestamp =  timestamp.strftime("%Y-%m-%d %H:%M:%S")


        with open("mood_historic.txt", "a+") as file:
            file.write(f"[{timestamp}:{user}] - {mood}\n")

        tracker.slots["mood_historic"] = mood

        # dispatcher.utter_message(text=f"Your mood '{mood}' have been recorded!")
        return [SlotSet("mood_historic", mood)]


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


class TriageForm(FormAction):

    def name(self):
        """Unique identifier of the form"""
        return "triage_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        risky = ['Sometimes', 'At least 3 times a week', 'Almost every day']
        safe = ['Almost never', 'Never']
        initial = ["anxiety_dsm", "drug_dsm", "depression_dsm", "mania_dsm", # inicio
                "psychosis_dsm", "dissociation_dsm", "suicide_dsm"]
        dassA = ["dassA1", "dassA2", "dassA3", "dassA4", "dassA5", "dassA6", "dassA7"]
        dassD = ["dassD1", "dassD2", "dassD3", "dassD4", "dassD5", "dassD6", "dassD7"]

        if tracker.get_slot('anxiety_dsm') in risky:
            if tracker.get_slot('drug_dsm') in safe:
                if tracker.

            initial.extend(dassA)
            return initial.extend(dassD)

        if


        else:
            return ["cuisine", "num_people",
                    "preferences", "feedback"]
        #return [
        #    "anxiety_dsm",
        #    "drug_dsm",
        #    "depression_dsm",
        #    "mania_dsm",
        #    "psychosis_dsm",
        #    "dissociation_dsm",
        #    "suicide_dsm",
        #]

    def slot_mappings(self):
        """A dictionary to map required slots to
        - an extracted entity
        - intent: value pairs
        - a whole message
        or a list of them, where a first match will be picked"""
        response = {
            "anxiety_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "drug_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "depression_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "mania_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "psychosis_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "dissociation_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],

            "suicide_dsm": [
                self.from_entity(
                    entity="scale_frequency", intent=["inform_scale"]
                ),
            ],
        }
        return(response)

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        dispatcher.utter_template("utter_end_triage", tracker)
        return []
