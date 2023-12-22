from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
        <html>
            <head>
                <title>Programming in Python</title>
            </head>
            <body>
                <h1>Hello World!</h1>
            </body>
        </html>
    '''


@app.route('/test')
def test():
    return 'Work in progress'
