from src.utils import conjugate_to_be, standard_construction, find_past_participle_form, find_continuous_form


def construct_present_simple(sentence_kind, subject, verb, object_phrase):
    auxiliary = "do" if subject in ["i", "you", "we", "they"] else "does"

    if sentence_kind == "Affirmative Sentence":
        if verb == "be":
            verb = conjugate_to_be(subject)
        else:
            if subject not in ["i", "you", "we", "they"]:
                verb = verb + "s"
        result = subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Interrogative Sentence":
        result = auxiliary + " " + subject + " " + verb + " " + object_phrase
    elif sentence_kind == "Negative Sentence":
        result = subject + " " + auxiliary + " not " + verb + " " + object_phrase
    else:
        result = "Unknown sentence kind: " + sentence_kind
    return result


def construct_present_continuous(sentence_kind, subject, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = conjugate_to_be(subject)
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_present_perfect(sentence_kind, subject, verb, object_phrase):
    verb = find_past_participle_form(verb)
    auxiliary = "have" if subject in ["i", "you", "we", "they"] else "has"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_present_perfect_continuous(sentence_kind, subject, verb, object_phrase):
    verb = find_continuous_form(verb)
    auxiliary = "have been" if subject in ["i", "you", "we", "they"] else "has been"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)
