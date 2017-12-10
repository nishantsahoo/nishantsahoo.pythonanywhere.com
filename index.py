import simplejson as json
import os
from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/', methods=["GET"])
def my_page():
	return send_from_directory("", 'index.html')

@app.route('/', methods=["POST"])
def my_page_result():
	return json.dumps(request.form)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3333))
	app.run(host='localhost', port=port, debug=True)
