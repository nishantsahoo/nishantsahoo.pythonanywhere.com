import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
	return "Hi there! This is Nishant Sahoo"

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3333))
	app.run(host='localhost', port=port, debug=True)
