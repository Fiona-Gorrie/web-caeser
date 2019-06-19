from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form="""
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
            <textarea name="text">
            </textarea>
            <input type="submit" value="Submit Query">
        </form>    
    
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/", method=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    encrypted_string = rotate_string(rot, text) 

    #Return the encrypted string wrapped in <h1> tags, to be rendered in the browser
    return encrypted_string

app.run()
