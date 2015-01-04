import re
import requests
import urllib2
from eatiht import v2


def zip_cookies(r):
	cookiedictkeys = r.cookies.keys()
	cookiedictvalues = r.cookies.values()
	for k, v in zip(cookiedictkeys, cookiedictvalues):
		cookiedict[k] = v
	return cookiedict
def input_date():
	bdinput = str(raw_input("Please enter a start date in the format MM/DD/YYYY: "))
	edinput = str(raw_input("Please enter an end date in the format MM/DD/YYYY: "))
	beginningdate = re.sub("/","%252F",bdinput)
	endingdate = re.sub("/","%252F",edinput)
def input_userdata():
	user = str(raw_input("Username: "))
	password = str(raw_input("Password: "))

input_date()
input_userdata()
cookiedict = {}
kronos = requests.Session()
kronos.cookies(cookiedict)
#see readme for details on reportindex and timeframeindex
reportindex = str(2)
timeframeindex = str(9)

#build the data, post it to wfc/portal. their server is broken, so we cant verify, but i dont care
loginparameters = {'LOGON_LOCALE_POLICY':'en', 'StartIndex':'0', 'authenticateWithSecurityQuestion':False, 'authenticateWithHRMSNewUserSetup':False, 'username':user, 'password':password, 'btnsubmit':True, 'returnUrl':'http://google.com', 'successUrl':'https://kronos-wfc.trinity-health.org/wfc/MyReportsDisplayServlet?', 'cancelUrl':'http://bing.com'}
login = requests.post("https://kronos-wfc.trinity-health.org/wfc/portal", data=loginparameters, allow_redirects=True, verify=False, auth=(user, password))

zip_cookies(login)

kronos = requests.get("https://kronos-wfc.trinity-health.org/wfc/applications/suitenav/navigation.do")

print "login request sent"
print login
print login.text

urlparameters = {'bd':beginningdate, 'ed':endingdate, 'reportindex':reportindex, 'timeframeindex':timeframeindex}
download = requests.get("https://kronos-wfc.trinity-health.org/wfc/MyReportsDisplayServlet?", auth=(user, password))

#download = "https://kronos-wfc.trinity-health.org/wfc/MyReportsDisplayServlet?reportindex=2&timeframeindex=9&bd=" + bd + "&ed=" + ed

#extracted_text = v2.extract(localdownload)
print download
print download.text