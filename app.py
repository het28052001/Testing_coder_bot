import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_html(filename):
    if os.path.exists(os.path.join('templates', filename)):
        return render_template(filename)
    else:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)