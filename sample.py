from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World"
    return name

@app.route('/good')
def good():
    name = "Good"
    name *= 5
    return render_template('hello.html', title='test', name=name)

## おまじない
if __name__ == "__main__":
    app.run(debug=False)