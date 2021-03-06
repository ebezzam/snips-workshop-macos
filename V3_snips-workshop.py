#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from hermes_python.hermes import Hermes
import pyowm
import io

INTENT_HOW_ARE_YOU = "bezzam:how_are_you"
INTENT_GOOD = "bezzam:feeling_good"
INTENT_BAD = "bezzam:feeling_bad"
INTENT_ALRIGHT = "bezzam:feeling_alright"
GET_TEMPERATURE = "bezzam:get_temperature"

API_KEY = 'api_key'

INTENT_FILTER_FEELING = [INTENT_GOOD, INTENT_BAD, INTENT_ALRIGHT]


def main():
    owm = pyowm.OWM(API_KEY)

    with Hermes("localhost:1883") as h:
        h.owm = owm
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .subscribe_intent(INTENT_GOOD, feeling_good_callback) \
         .subscribe_intent(INTENT_BAD, feeling_bad_callback) \
         .subscribe_intent(INTENT_ALRIGHT, feeling_alright_callback) \
         .subscribe_intent(GET_TEMPERATURE, get_temperature_callback) \
         .start()

def get_temperature_callback(hermes, intent_message):
    session_id = intent_message.session_id

    city = intent_message.slots.city.first().value
    try:
        observation = hermes.owm.weather_at_place(city)
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]
        response = "It's {} degrees in {}.".format(temp, city)
    except:
        response = "You asked for the temperature in {}.".format(city)
    hermes.publish_end_session(session_id, response)

def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "I'm doing great. How about you?"
    hermes.publish_continue_session(session_id, response, INTENT_FILTER_FEELING)


def feeling_good_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "That's awesome! I'm happy to hear that."
    hermes.publish_end_session(session_id, response)


def feeling_bad_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Sorry to hear that. I hope you feel better soon."
    hermes.publish_end_session(session_id, response)


def feeling_alright_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "That's cool."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
