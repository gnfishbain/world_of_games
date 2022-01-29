from flask import Flask
from Score import get_score


app = Flask(__name__)

@app.route("/<name>/")
def score_server(name):
    try:
        SCORE= get_score(name)

        return f"""<html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{SCORE}</div></h1>
        </body>
        </html>"""

    except Exception as e:
        ERROR= e

        return f"""<html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <body>
        <h1><div id="score" style="color:red">{ERROR}</div></h1>
        </body>
        </html>"""

@app.route("/api/score/<name>")
def api(name=None):
    return """<p id="number">{}</p>""".format(get_score(name))

app.run(debug=True)
