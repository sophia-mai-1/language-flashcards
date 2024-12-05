from flask import Flask, render_template, request, redirect, url_for
from functions import get_pinyin, get_translation, get_definition

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/flashcard', methods=['POST'])
def create_flashcard():
    chinese_text = request.form.get('chinese_text')

    if not chinese_text:
        return "Please provide Chinese text.", 400

    pinyin_result = get_pinyin(chinese_text)
    translation_result = get_translation(chinese_text)

    definition_result = None
    if translation_result and isinstance(translation_result, list):
        definition_result = get_definition(translation_result)
    elif translation_result and isinstance(translation_result, str):
        translation_result = [translation_result]

    return render_template(
        'flashcard.html',
        chinese_text=chinese_text,
        pinyin=pinyin_result,
        translation=", ".join(translation_result) if isinstance(translation_result, list) else translation_result,
        definition=definition_result
    )

if __name__ == "__main__":
    app.run(debug=True)
