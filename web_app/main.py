from flask import Flask, render_template

app = Flask(__name__)  # Changed _name_ to __name__

@app.route('/')
def home():
    return render_template('index.html', title="Home page")

if __name__ == '__main__': # This also requires double underscores
    app.run(host='127.0.0.1', port=8080, debug=True)
