from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/square/<int:n>')
def findSquare(n):
    result = {
        "Number" : n,
        "Square" : n*n,
    }
    return result

if( __name__ == "__main__"):
    app.run(debug = True)