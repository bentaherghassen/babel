from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = ['en', 'fr', 'ar']

babel = Babel(app, locale_selector=lambda: request.args.get('lang') or 'en')

@app.route('/')
def index():
    greeting = _('Hello, welcome to our Flask app!')
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
