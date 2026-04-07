from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Ensure this is indented (usually 4 spaces)
    return render_template('index.html', title="Home page")

if __name__ == '__main__':
    # Ensure this is indented under the 'if' block
    app.run(host='127.0.0.1', port=8080, debug=True)
