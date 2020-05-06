## greet + facility_search + location
* greet
  - utter_how_can_i_help
* search_provider{"facility": "hospital"}
  - utter_ask_location
* inform{"location": "San Francisco"}
  - action_facility_search
  - slot{"address": "random address"}
* thanks
  - utter_goodbye

## search hospital happy path
* greet
  - utter_how_can_i_help
* search_provider{"facility": "hospital", "location": "Brasilia"}
  - action_facility_search
  - slot{"address": "random address"}
* thanks
  - utter_goodbye

## greet + get name + check mood
* greet
  - utter_greet
  - utter_ask_name
* inform_name{"name": "name"}
  - utter_name
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - action_debug_bot
  - slot{"mood": "mood"}
  - utter_user_mood

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
