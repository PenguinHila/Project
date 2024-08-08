from flask import Flask
import os



app = Flask(__name__)

@app.route("/")
def score_server():
# A string representing a file name.
SCORES_FILE_NAME = "score.txt"

# A number representing a bad return code for a function.
BAD_RETURN_CODE = 666
    
    try:
        if os.path.exists(SCORES_FILE_NAME):
            with open(SCORES_FILE_NAME, 'r') as file:
                SCORE = int(file.readline())
                return f"""<html>
                                <head>
                                    <title>Score game</title>
                                </head>
                                <body>
                                    <h1>The score is:</h1>
                                    <div id="score">{SCORE}</div>
                                </body>
                                </html>"""
        else:
            return f"""<html>
                            <head>
                                <title>Score game</title>
                            </head>
                            <body>
                                <h1>ERROR</h1>
                                <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                            </body>
                            </html>"""
    except (FileNotFoundError, ValueError):
        return f"""<html>
                                    <head>
                                        <title>Score game</title>
                                    </head>
                                    <body>
                                        <h1>ERROR</h1>
                                        <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                                    </body>
                                    </html>"""


#if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000, debug=True)


