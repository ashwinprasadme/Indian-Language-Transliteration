from flask import Flask,render_template
from indictrans import Transliterator

app=Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.route('/')
@app.route('/<name>')
def index(name):
    eng = name    
    lang = ["hin", "guj", "pan", "ben", "mal", "kan", "tam", "tel", "ori", "mar", "kok", "asm", "urd"]
    transliterated = {}
    for language in lang:
        trn = Transliterator(source='eng', target=language, build_lookup=True)
        tmp_trlt = trn.transform(eng)
        transliterated[language] = tmp_trlt
    print transliterated

    return render_template('index.html',
        english = eng,
        hindi = transliterated["hin"],
        kannada = transliterated["kan"],
        bengali = transliterated["ben"],
        gujarati = transliterated["guj"],
        punjabi = transliterated["pan"],
        malayalam = transliterated["mal"],
        tamil = transliterated["tam"],
        telegu = transliterated["tel"],
        assamese = transliterated["asm"],
        urdu = transliterated["urd"]
        )
