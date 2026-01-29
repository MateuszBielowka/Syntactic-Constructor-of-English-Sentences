# Syntactic Constructor of English Sentences

A web-based application designed to programmatically construct grammatically correct English sentences. The tool applies specific linguistic rules to transform base components (subjects, verbs, objects) into full sentences across various tenses.

## Key Features
- **Tense-Based Generation**: Dynamically constructs sentences in Past, Present, and Future tenses.
- **Syntactic Rule Engine**: Handles complex conjugation rules (e.g., third-person singular "s", irregular verb forms, and auxiliary verb placement).
- **Modular Design**: Separate modules for different tense groups allow for easy expansion of the grammar ruleset.
- **Interactive UI**: A clean web interface allowing users to select parameters and see generated results in real-time.

## Project Structure
- **data/**: Contains dictionaries or word lists used as building blocks for sentences.
- **static/ & templates/**: Web interface files, including CSS for styling and HTML for the UI.
- **app.py**: The Flask backend that handles routing and user input.
- **sentence_constructor.py**: The central engine that coordinates the assembly of sentence parts.
- **present_tenses_construction.py**: Logic and rules for Present Simple, Continuous, Perfect, etc.
- **past_tenses_construction.py**: Logic and rules for Past Simple, Continuous, and Perfect forms.
- **future_tenses_construction.py**: Logic and rules for various future-tense structures.
- **package.json**: Manages frontend dependencies and scripts.

## Technologies
- **Language**: Python 3.10+
- **Web Framework**: Flask 3.0
- **Frontend**: HTML, CSS, JavaScript
- **Package Management**: Node.js/NPM (for frontend assets)
- **Logic**: Custom algorithmic implementation of English grammar rules.

## Results
The constructor provides a reliable framework for generating syntactically sound English sentences. It moves beyond simple "template filling" by using modular scripts to handle the nuances of English conjugation and syntax. The result is an educational and functional tool that demonstrates the intersection of programming logic and natural language processing (NLP).
