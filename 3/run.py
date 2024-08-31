from flask import Flask
#print(__name__)
#__name__ ist der Modulname, in diesem Fall "run"
app = Flask(__name__)

#Dekorierer
#damit wird die Funktion "hello_world" aufgerufen, sobald die Startseite aufgerufen wird
@app.route("/")
def hello_world():
    return "Hello, World!"

#ruft die Function "test_function" auf, wenn "http://127.0.0.1:5000/test" aufgerufen wird
@app.route("/test")
def test_function():
    paragraph = "<p>Hello World</p>"
    return "Hello <strong>Test</strong> Function" + paragraph