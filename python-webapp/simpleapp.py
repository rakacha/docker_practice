from flask import Flask
import optparse

app = Flask(__name__)


@app.route("/")
def hello_world():

    return "Hello world from Python!"


if __name__ == "__main__":

    parser = optparse.OptionParser(usage="python simpleapp.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port')
    (args, _) = parser.parse_args()
    app.run(host='0.0.0.0', port=int(args.port), debug=True)
