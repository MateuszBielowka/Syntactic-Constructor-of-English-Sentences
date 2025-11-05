import json


def convert_csv_to_json(filepath):
    with open(f'{filepath}.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with open(f'{filepath}.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(list(content.split(',')), jsonfile, indent=4)


def standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary):
    if sentence_kind == "Interrogative Sentence":
        return auxiliary + " " + subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Affirmative Sentence":
        return subject + " " + auxiliary + " " + verb + " " + object_phrase
    elif sentence_kind == "Negative Sentence":
        return subject + " " + auxiliary + " not " + verb + " " + object_phrase
    else:
        return "Unknown sentence kind: " + sentence_kind


def conjugate_to_be(person):
    conjugation_table = {
        "i": "am",
        "you": "are",
        "he": "is",
        "she": "is",
        "it": "is",
        "we": "are",
        "they": "are"
    }
    return conjugation_table[person.lower()]


def find_continuous_form(verb):
    if len(verb) > 2 and verb[-1] == 'e' and verb[-2] != 'e':
        verb = verb[:-1]
    elif len(verb) == 3 and verb[-1] == 't':
        verb = verb + 't'
    return verb + "ing"


def find_past_simple_form(verb):
    # TODO: write this function so it imports something and returns a correct form
    return "TODO"


def find_past_participle_form(verb):
    # TODO: write this function so it imports something and returns a correct form
    return "TODO"
