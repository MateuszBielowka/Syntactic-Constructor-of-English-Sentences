from src.utils import conjugate_to_be, standard_construction, find_past_simple_form, find_continuous_form


def construct_past_simple(sentence_kind, subject, plural, verb, object_phrase):
    auxiliary = "did"
    if sentence_kind == "Affirmative Sentence":
        verb = find_past_simple_form(verb)
        result = subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Interrogative Sentence":
        if verb == "be":
            verb = "were" if subject in ["you", "we", "they"] or plural else "was"
            result = verb + " " + subject + " " + object_phrase
        else:
            result = auxiliary + " " + subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Negative Sentence":
        if verb == "be":
            verb = "were" if subject in ["you", "we", "they"] or plural else "was"
            result = subject + " " + verb + " not " + object_phrase
        else:
            result = subject + " " + auxiliary + " not " + verb + " " + object_phrase
    else:
        result = "Unknown sentence kind: " + sentence_kind
    return result


def construct_past_continuous(sentence_kind, subject, plural, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = "were" if subject in ["you", "we", "they"] or plural else "was"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)



def construct_past_perfect(sentence_kind, subject, plural, verb, object_phrase):
    verb = find_past_simple_form(verb)
    auxiliary = "had"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_past_perfect_continuous(sentence_kind, subject, plural, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = "had been"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)