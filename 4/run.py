from flask import Flask, render_template

#print(__name__)
#__name__ ist der Modulname, in diesem Fall "run"
app = Flask(__name__)

#Dekorierer
#damit wird die Funktion "hello_world" aufgerufen, sobald die Startseite aufgerufen wird
@app.route("/")
def hello_world():
    items = ["Apfel", "Birne", "Banane"]
    #ruft die start.html Datei aus dem Ordner "templates" auf, mit den zusätzlichen Parametern. In der HTML Datei muss der Parametername gleich sein
    return render_template("start.html", name = "Max Mustermann", items=items)

#ruft die Function "test_function" auf, wenn "http://127.0.0.1:5000/test" aufgerufen wird
@app.route("/test")
def test_function():
    paragraph = "<p>Hello World</p>"
    return "Hello <strong>Test</strong> Function" + paragraph