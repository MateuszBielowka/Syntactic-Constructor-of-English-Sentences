from flask import Flask, render_template, jsonify, send_from_directory, request
from pathlib import Path
import json

app = Flask(__name__)

RESULTS_PATH = Path('data')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/noun_list")
def jsonify_nouns():
    return jsonify(json.loads((RESULTS_PATH / "english_nouns.json").read_text()))

@app.route("/api/verb_list")
def jsonify_verbs():
    return jsonify(json.loads((RESULTS_PATH / "english_verbs.json").read_text()))

@app.route("/api/adjective_list")
def jsonify_adjectives():
    return jsonify(json.loads((RESULTS_PATH / "english_adjectives.json").read_text()))

@app.route("/api/pronoun_list")
def jsonify_pronouns():
    return jsonify(json.loads((RESULTS_PATH / "english_pronouns.json").read_text()))

@app.route("/api/tense_list")
def jsonify_tenses():
    return jsonify(json.loads((RESULTS_PATH / "english_tenses.json").read_text()))

@app.route("/api/sentence_kind_list")
def jsonify_sentence_kinds():
    return jsonify(json.loads((RESULTS_PATH / "english_sentence_kinds.json").read_text()))

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    # do usuniecia
    for key in data:
        data[key] = data[key][0]
    result = data
    print(result)
    # koniec testu
    #TODO wywołanie funkcji zmieniającej data w poprawne zdanie (zwracamy string result)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
