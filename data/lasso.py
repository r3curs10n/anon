import os
import sys
import cPickle
from Dataset import Dataset

sys.path.append('/usr/local/lib/python2.7/site-packages')

import pymysql as MySQLdb

HOST = '172.16.27.31'
USER = 'root'
PASS = ''
DBNAME = 'AI'

print '''
1. Clone
2. Update
'''

def getDB():
	return MySQLdb.connect(HOST, USER, PASS, DBNAME)

def clone():
	print 'Enter name for new dataset:'
	dsname = raw_input()

	os.system('mkdir %s' % dsname)
	ds = Dataset()
	db = getDB()
	cur = db.cursor(MySQLdb.cursors.DictCursor)

	cur.execute("SELECT * FROM Answers WHERE isRetrieved=1")
	for row in cur.fetchall():
		ds.X.append(row['answer'])
		ds.Y.append(row['author'])
		ds.ts = max([ds.ts, row['updated_at']])

	with open('%s/data' % dsname, 'w') as f:
		cPickle.dump(ds, f)
	print 'Dataset cloned'

def update():
	print 'Enter dataset to update'
	dsname = raw_input()

	f = open('%s/data' % dsname, 'r')
	ds = cPickle.load(f)
	f.close()
	ts = ds.ts

	db = getDB()
	cur = db.cursor(MySQLdb.cursors.DictCursor)

	cur.execute("SELECT * FROM Answers WHERE isRetrieved=1 AND updated_at > %d" % ts)
	for row in cur.fetchall():
		ds.X.append(row['answer'])
		ds.Y.append(row['author'])
		ds.ts = max([ds.ts, row['updated_at']])

	with open('%s/data' % dsname, 'w') as f:
		cPickle.dump(ds, f)
	print 'Dataset updated'

if __name__=='__main__':
	action = int(raw_input())

	if action == 1:
		clone()
	elif action == 2:
		update()