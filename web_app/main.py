from flask import Flask, render_template

# CRITICAL: Use double underscores __ on both sides of name
app = Flask(__name__):

@app.route('/')
def home():
    return render_template('index.html', title="Home page")

# CRITICAL: Use double underscores for __name__ and __main__
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
