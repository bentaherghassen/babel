# Flask Greeting App (Multilingual)

A simple Flask app using Flask-Babel for translations (English, French, Arabic).

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install Flask Flask-Babel
```

2. Run the app:

```bash
python app.py
```

Then visit:
- English: http://127.0.0.1:5000/?lang=en
- French:  http://127.0.0.1:5000/?lang=fr
- Arabic:  http://127.0.0.1:5000/?lang=ar

## Rebuilding Translations (optional)

If you edit messages:

```bash
pybabel extract -F babel.cfg -o messages.pot .
pybabel update -i messages.pot -d translations
pybabel compile -d translations
```
