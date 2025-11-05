import json
import os


def convert_csv_to_json(filepath):
    with open(f'{filepath}.csv', mode='r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    with open(f'{filepath}.json', mode='w', encoding='utf-8') as jsonfile:
        json.dump(list(content.split(',')), jsonfile, indent=4)


def load_irregular_verbs(filepath):
    with open(f'{filepath}.json', mode='r', encoding='utf-8', errors='ignore') as f:
        irregular_verbs = f.read()
    return irregular_verbs


def find_second_form(verb):
    #TODO
    return ''

def find_third_form(verb):
    #TODO
    return ''


def construct_verb(subject, plural, verb, tense):
    person_list = ['i', 'you', 'he', 'she', 'we', 'they']
    present_dict = {'i': 'am', 'you': 'are', 'he': 'is', 'she': 'is', 'we': 'are', 'they': 'are'}
    past_dict = {'i': 'was', 'you': 'were', 'he': 'was', 'she': 'was', 'we': 'were', 'they': 'were'}
    have_dict = {'i': 'have', 'you': 'have', 'he': 'has', 'she': 'has', 'we': 'have', 'they': 'have'}

    if tense == "Present Simple":
        if verb == 'be':
            verb = present_dict[subject]
        elif verb == 'have':
            verb = have_dict[subject]
        elif subject in ['he', 'she'] or plural is False:
            if verb[-1] == 'o':
                verb = verb + 'e'
            verb = verb + 's'
    if tense == "Present Continuous":
        if subject in person_list:
            verb = present_dict[subject] + verb + 'ing'
        if plural is False:
            verb = 'is ' + verb + 'ing'
        if plural is True:
            verb = 'are ' + verb + 'ing'
    if tense == "Present Perfect":  # TODO third form
        if subject in ['he', 'she'] or plural is False:
            verb = 'has ' + verb
        else:
            verb = 'have ' + verb
    if tense == "Present Perfect Continuous":
        if subject in ['he', 'she'] or plural is False:
            verb = 'has been ' + verb + 'ing'
        else:
            verb = 'have been ' + verb + 'ing'
    if tense == "Past Simple":
        # TODO second form
        pass
    if tense == "Past Continuous":
        if subject in person_list:
            verb = past_dict[subject] + verb + 'ing'
        if plural is False:
            verb = 'was ' + verb + 'ing'
        if plural is True:
            verb = 'were ' + verb + 'ing'
    if tense == "Past Perfect":
        verb = 'had ' + verb  # TODO third form
    if tense == "Past Perfect Continuous":
        verb = 'had been ' + verb + 'ing'
    if tense == "Future simple":
        verb = 'will ' + verb
    if tense == "Future Continuous":
        verb = 'will be ' + verb + 'ing'
    if tense == "Future Perfect":
        verb = 'will have ' + verb  # TODO third form
    if tense == "Future Perfect Continuous":
        verb = 'will have been' + verb + 'ing'
        
    return verb


def construct_sentence(sub, plural, obj, ver, adj, pro, tense, s_k):
    subject = sub
    object = obj
    adjective = adj
    pronoun = pro

    load_irregular_verbs()
    
    verb = construct_verb(subject, plural, ver, tense)

    final_sentence = f'{subject} {verb}'
    if s_k == "Zdanie pytające":
        if tense == "Present Simple":
            if subject in ['he', 'she'] or plural is False:
                final_sentence = f'Does {subject} {verb}'
            else:
                final_sentence = f'Do {subject} {verb}'
        elif tense == "Past Simple":
            final_sentence = f'Did {subject} {ver}'
        else:
            final_sentence = list(final_sentence) # I had been going; she has done
            final_sentence.insert(0, final_sentence.pop(1))
    elif s_k == "Zdanie przeczące":
        if tense == "Present Simple":
            if subject in ['he', 'she'] or plural is False:
                final_sentence = f'{subject} does not {verb}'
            else:
                final_sentence = f'{subject} do not {verb}'
        elif tense == "Past Simple":
            final_sentence = f'{subject} did not {ver}'
        else:
            final_sentence = list(final_sentence) # I had not been going; she has not done
            final_sentence.insert(2, 'not')
        pass
    else:
        pass
        #TODO

    if pronoun == 'null':
        final_sentence += ' the'
    else:
        final_sentence += f' {pronoun}'
    if adjective != 'null':
        final_sentence += f' {adjective}'
    final_sentence += f' {object}'

    return final_sentence
