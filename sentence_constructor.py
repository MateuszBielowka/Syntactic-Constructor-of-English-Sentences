import os

from src.utils import (
    convert_csv_to_json
)
from present_tenses_construction import(
    construct_present_simple,
    construct_present_continuous,
    construct_present_perfect,
    construct_present_perfect_continuous
)
from past_tenses_construction import(
    construct_past_simple,
    construct_past_continuous,
    construct_past_perfect,
    construct_past_perfect_continuous
)
from future_tenses_construction import(
    construct_future_simple,
    construct_future_continuous,
    construct_future_perfect,
    construct_future_perfect_continuous
)

TENSE_FUNCTIONS = {
    "Present Simple": construct_present_simple,
    "Present Continuous": construct_present_continuous,
    "Present Perfect": construct_present_perfect,
    "Present Perfect Continuous": construct_present_perfect_continuous,
    "Past Simple": construct_past_simple,
    "Past Continuous": construct_past_continuous,
    "Past Perfect": construct_past_perfect,
    "Past Perfect Continuous": construct_past_perfect_continuous,
    "Future Simple": construct_future_simple,
    "Future Continuous": construct_future_continuous,
    "Future Perfect": construct_future_perfect,
    "Future Perfect Continuous": construct_future_perfect_continuous,
}


def construct_sentence(sentence):
    subject = sentence['subject']
    verb = sentence['verb']
    object_phrase = sentence['object']
    tense = sentence['tense']
    sentence_kind = sentence['sentence_kind']
    adjective = sentence['adjective']
    pronoun = sentence['pronoun']

    if adjective != 'null':
        object_phrase = object_phrase + ' ' + adjective
    if pronoun != 'null':
        object_phrase = pronoun + ' ' + object_phrase

    constructor = TENSE_FUNCTIONS.get(tense)

    if constructor:
        sentence = constructor(sentence_kind, subject, verb, object_phrase)
        return sentence.capitalize().replace("i ", "I ")
    else:
        return "Unsupported tense: " + str(tense)
