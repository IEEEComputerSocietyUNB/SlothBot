<!-- ## greet + get name + check mood
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
  - slot{"triage": "triage"}
  - utter_triage_choice -->


## greet + name + demographic
* greet
  - utter_greet
  - utter_ask_name
* inform_name{"name": "name"}
  - utter_name
  - utter_ask_demographic
* affirm
  - demographic_form
  - slot{"age": 22}
  - slot{"gender": "Male"}
  - slot{"timeunb": 3}
  - slot{"neighborhood": "DF"}
  - slot{"therapy": false}
  - slot{"work": false}
  - slot{"major": "Engineer"}
  - slot{"ethnicity": asian}
  - action_debug_bot

<!--* inform_age{"age":"age"}
  - utter_ask_gender
* inform_gender{"gender":"gender"}
  - utter_ask_neighborhood
* inform_neighborhood{"neighborhood":"neighborhood"}
  - utter_ask_therapy
* inform_therapy{"therapy":"therapy"}
  - utter_ask_ethnicity
* inform_therapy{"ethnicity":"ethnicity"}
  - utter_ask_work
* inform_work{"work":"work"}
  - utter_ask_major
* inform_major{"major":"major"}
  - utter_ask_timeunb
* inform_timeunb{"timeunb":"timeunb"}
-->

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
