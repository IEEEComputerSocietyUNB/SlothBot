## greet + get name + check mood
* greet
  - utter_greet
  - utter_ask_name
* inform_name{"name": "name"}
  - utter_name
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - slot{"mood": "mood"}
  - utter_ask_triage
* inform_triage{"triage": "triage"}
  - action_debug_bot
  - slot{"triage": "triage"}
  - utter_triage_choice

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
