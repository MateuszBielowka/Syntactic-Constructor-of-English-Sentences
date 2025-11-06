from src.utils import conjugate_to_be, standard_construction, find_past_simple_form, find_continuous_form


def construct_future_simple(sentence_kind, subject, plural, verb, object_phrase):
    auxiliary = "will"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)



def construct_future_continuous(sentence_kind, subject, plural, verb, object_phrase):
    verb = "be " + find_continuous_form(verb)
    auxiliary = "will"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_future_perfect(sentence_kind, subject, plural, verb, object_phrase):
    verb = "have " + find_past_simple_form(verb)
    auxiliary = "will"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)


def construct_future_perfect_continuous(sentence_kind, subject, plural, verb, object_phrase):
    verb = "have been " + find_continuous_form(verb)
    auxiliary = "will"
    return standard_construction(sentence_kind, subject, verb, object_phrase, auxiliary)