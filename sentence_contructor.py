import os

from src.utils import (
    convert_csv_to_json, load_irregular_verbs
)

def main():
    path = os.path.join(os.path.dirname(__file__), 'data')

    # convert_csv_to_json(f'{path}\\english_nouns')
    # convert_csv_to_json(f'{path}\\english_verbs')
    # convert_csv_to_json(f'{path}\\english_adjectives')
    # convert_csv_to_json(f'{path}\\english_pronouns')
    # convert_csv_to_json(f'{path}\\english_tenses')
    # convert_csv_to_json(f'{path}\\english_sentence_kinds')

    path = os.path.join(os.path.dirname(__file__), 'data')
    iv = load_irregular_verbs(f'{path}\\irregular_verbs')
    print(iv[0])


if __name__ == "__main__":
    main()