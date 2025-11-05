from src.utils import conjugate_to_be, standard_construction, find_past_simple_form, find_continuous_form


def construct_past_simple(sentence_kind, subject, verb, object_phrase):
    auxilliary = "did"
    if sentence_kind == "Affirmative Sentence":
        verb = find_past_simple_form(verb)
        result = subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Interrogative Sentence":
        result = auxilliary + " " + subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Negative Sentence":
        result = subject + " " + auxilliary + " not " + verb + " " + object_phrase
    else:
        result = "Unknown sentence kind: " + sentence_kind
    return result


def construct_past_continuous(sentence_kind, subject, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = "were" if subject in ["you", "we", "they"] else "was"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)



def construct_past_perfect(sentence_kind, subject, verb, object_phrase):
    verb = find_past_simple_form(verb)
    auxiliary = "had"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_past_perfect_continuous(sentence_kind, subject, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = "had been"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)