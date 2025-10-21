import os

from src.utils import (
    convert_csv_to_json
)

def main():
    path = os.path.join(os.path.dirname(__file__), 'data')

    # convert_csv_to_json(f'{path}\\english_nouns')
    # convert_csv_to_json(f'{path}\\english_verbs')
    # convert_csv_to_json(f'{path}\\english_adjectives')
    # convert_csv_to_json(f'{path}\\english_pronouns')
    # convert_csv_to_json(f'{path}\\english_tenses')
    # convert_csv_to_json(f'{path}\\english_sentence_kinds')



if __name__ == "__main__":
    main()