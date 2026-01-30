# Syntactic Constructor of English Sentences

## 🎓 Project Description
A web-based application designed to programmatically construct grammatically correct English sentences. The tool applies specific linguistic rules to transform base components (subjects, verbs, objects) into full sentences across various tenses.

## 🔑 Key Features
- **Tense-Based Generation**: Dynamically constructs sentences in Past, Present, and Future tenses.
- **Syntactic Rule Engine**: Handles complex conjugation rules (e.g., third-person singular "s", irregular verb forms, and auxiliary verb placement).
- **Modular Design**: Separate modules for different tense groups allow for easy expansion of the grammar ruleset.
- **Interactive UI**: A clean web interface allowing users to select parameters and see generated results in real-time.

## 🧪  Technology
- **Language**: Python 3.10+
- **Web Framework**: Flask 3.0
- **Frontend**: HTML, CSS, JavaScript, Node.js
- **Logic**: Custom algorithmic implementation of English grammar rules.

## 📝 Project Structure
```
├── data/
│   ├── english_adjectives.csv
│   ├── english_adjectives.json
│   ├── english_nouns.csv
│   ├── english_nouns.json
│   ├── english_pronouns.csv
│   ├── english_pronouns.json
│   ├── english_sentence_kinds.csv
│   ├── english_sentence_kinds.json
│   ├── english_tenses.csv
│   ├── english_tenses.json
│   ├── english_verbs.csv
│   ├── english_verbs.json
│   └── irregular_verbs.json
├── src/
│   └── utils.py
├── static/
│   ├── scripts.js
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── future_tenses_construction.py
├── package.json
├── past_tenses_construction.py
├── present_tenses_construction.py
├── sentence_constructor.py
└── README.md
```

## 🔬 Results
The constructor provides a reliable framework for generating syntactically sound English sentences. It moves beyond simple "template filling" by using modular scripts to handle the nuances of English conjugation and syntax. The result is an educational and functional tool that demonstrates the intersection of programming logic and natural language processing.

### Affirmative sentence:
<img width="1311" height="221" alt="image" src="https://github.com/user-attachments/assets/19feee77-e41c-483e-86ea-c4d241a13865" />

### Question:
<img width="1295" height="227" alt="image" src="https://github.com/user-attachments/assets/0013de06-1d26-4044-ae53-d87e55515be0" />

### Negative sentence:
<img width="1291" height="226" alt="image" src="https://github.com/user-attachments/assets/25f2bc48-5280-4944-9c59-cd79f6b6ba57" />

## 📷 Example Screenshots
<img width="1329" height="806" alt="image" src="https://github.com/user-attachments/assets/60eeea79-2039-4621-95f7-fcea5400a8be" />

<img width="1338" height="802" alt="image" src="https://github.com/user-attachments/assets/997eb3fc-9a28-446c-b9a6-5184c244eb59" />
