from bs4 import BeautifulSoup
import urllib2
import MySQLdb
import sys


def setupProxy(proxy, username, password):
	if username == "":
		proxy = urllib2.ProxyHandler({'http': proxy})
		opener = urllib2.build_opener(proxy)
		urllib2.install_opener(opener)
	else:
		proxy = urllib2.ProxyHandler({'http': 'http://'+ username + ':' + password + '@' + proxy})
		auth = urllib2.HTTPBasicAuthHandler()
		opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
		urllib2.install_opener(opener)

#db specifications
host = "localhost"
user = "root"
passwd = "asdf"
database = "AI"

def getSoup(url):
	content = urllib2.urlopen(url).read()
	return BeautifulSoup(content)


def gc(x,tag):
	return [i for i in tag][x]

class Navigator:
	def __init__(self, bs):
		self.bs = bs
	def getChild(self, i):
		self.bs = gc(i, self.bs)
		return self

def getAnswerText(url):
	soup = getSoup(url)
	answer = soup.findAll(attrs={'class':"AnswerStandalone"})[0]
	navigate = Navigator(answer)	
	return navigate.getChild(0).getChild(0).getChild(2).getChild(1).getChild(0).getChild(0).getChild(0).bs.get_text()


def removeNonAscii(s):
	return "".join(i for i in s if ord(i)<128)


def fetchAnswers(proxy, username, password):

	setupProxy(proxy, username, password)

	db = MySQLdb.connect(host, user, passwd, database)
	select_cursor = db.cursor()
	update_cursor = db.cursor()

	while True: #until any answer with isRetrieved = False is present
		select_cursor.execute("Select permalink from Answers where isRetrieved = False")
		update_cursor.execute("Prepare Query from 'Update Answers set answer = ? , isRetrieved = True where permalink = ?'")

		unretrieved_count = 0
		for permalink in select_cursor.fetchall():
			permalink = permalink[0]
			answer = removeNonAscii(getAnswerText(permalink))
			update_cursor.execute("Set @answer = %s",(answer))
			update_cursor.execute("Set @permalink = %s", (permalink))
			try: 
				update_cursor.execute("Execute Query using @answer, @permalink")
			except Exception as e:
				print query
				print e

			unretrieved_count += 1

		db.commit()

		if unretrieved_count == 0:
			break

# Run : python fetchAnswers.py proxy:port-username-password (Ex- python fetchAnswers.py 202.141.80.19:3128-xyz-abc)
# If using proxy which does not need authentication then, python fetchAnswers.py proxy:port-- (Ex- python fetchAnswers.py 172.16.27.xx:abcd--) 
(proxy,username,password) = (sys.argv[1]).split('-') 
fetchAnswers(proxy, username, password)
