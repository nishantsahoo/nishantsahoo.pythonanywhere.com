import simplejson as json
import os
from flask import Flask, request, send_from_directory
from bs4 import BeautifulSoup
import mechanize

app = Flask(__name__, static_url_path='')

@app.route('/', methods=["GET"])
def my_page():
	return send_from_directory("", 'index.html')

@app.route('/', methods=["POST"])
def my_page_result():
	userId   = request.form['username']
	password = request.form['password']

	url           = "http://slcm.manipal.edu/loginForm.aspx"
	browserObject = mechanize.Browser()
	response      = browserObject.open(url)

	browserObject.select_form("form1")
	browserObject.form['txtUserid']   = userId
	browserObject.form['txtpassword'] = password
	browserObject.method              = "POST"

	response   = browserObject.submit()
	print response.code # status is always 200 ._.
	response   = browserObject.open("http://slcm.manipal.edu/Academics.aspx")
	academics  = BeautifulSoup(response.read(), "html5lib")

	attendance_dict = {}

	table_attendance = academics.find('table', attrs={'id':'tblAttendancePercentage'})
	tbody = table_attendance.find('tbody')
	tr_list = tbody.findAll('tr')

	for tr in tr_list:
		td_list = tr.findAll('td')[1:]
		attendance_dict[td_list[0].text] = {
			'name':       td_list[1].text,
			'total':      td_list[3].text,
			'present': 	  td_list[4].text,
			'absent':     td_list[5].text,
			'percentage': td_list[6].text
		}

	print json.dumps(attendance_dict, indent=4, sort_keys=True)

	return json.dumps(attendance_dict, indent=4, sort_keys=True)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 3333))
	app.run(host='localhost', port=port, debug=True)
