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
  - utter_triage_choice
  - action_debug_bot


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
  - slot{"neighborhood": "DF"}
  - slot{"therapy": false}
  - slot{"ethnicity": "asian"}
  - slot{"work": false}
  - slot{"major": "Engineer"}
  - slot{"timeunb": 3}
  - utter_continue
* affirm
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - slot{"mood": "mood"}
  - action_store_mood
  - slot{"mood_historic":"mood_historic"}
  - utter_ask_mood_historic
* affirm
  - utter_mood_h
-->

## greet + no name + no_demographic + mood
* greet
  - utter_greet
  - utter_ask_name
* inform_name{"name": "None"}
  - utter_name
  - utter_ask_demographic
* deny
  - utter_continue
* affirm
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - action_store_mood
  - slot{"mood_historic":"mood"}
  - utter_mood_feedback
  - utter_ask_show_mood_historic
* affirm
  - utter_mood_historic
  - utter_continue
* affirm
  - utter_ask_screening
* affirm
  - screening_form
  - slot{"anxiety_dsm":"anxiety_dsm"}
  - slot{"drug_dsm":"drug_dsm"}
  - slot{"depression_dsm":"depression_dsm"}
  - slot{"mania_dsm":"mania_dsm"}
  - slot{"psychosis_dsm":"psychosis_dsm"}
  - slot{"dissociation_dsm":"dissociation_dsm"}
  - slot{"suicide_dsm":"suicide_dsm"}
  - utter_continue




## greet + name + no_demographic + mood
  * greet
    - slot{"name": "name"}
    - utter_greet_name
    - utter_ask_mood
  * inform_mood{"mood": "mood"}
    - action_store_mood
    - slot{"mood_historic":"mood"}
    - utter_mood_feedback
    - utter_ask_show_mood_historic
  * affirm
    - utter_mood_historic


<!--
* inform_mood{"mood": "mood"}
## greet + mood + triage
* greet
  - slot{"name":"name"}
  - utter_greet
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - slot{"mood": "mood"}
  - utter_mood_feedback
  - utter_continue
* affirm
  - utter_ask_triage
* affirm
  - utter_goodbye

## greet + mood + no_triage
* greet
  - slot{"name":"name"}
  - utter_greet
  - utter_ask_mood
* inform_mood{"mood": "mood"}
  - slot{"mood": "mood"}
  - utter_mood_feedback
  - utter_continue
* affirm
  - utter_ask_triage
* deny
  - utter_goodbye
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
