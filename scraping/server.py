import BaseHTTPServer
import time
import cgi
import MySQLdb

HOST_NAME = '0.0.0.0'
PORT_NUMBER = 8080

def get_author(permalink):
    return permalink.split('/')[-1]

def insert_db(db, author, permalink):
    cursor = db.cursor()
    
    sql = """INSERT INTO Answers(permalink,
             author, answer)
             VALUES ('%s', '%s', '')""" % (permalink, author)
    try:
       cursor.execute(sql)
       db.commit()
    except:
        pass

def dump_data(permalinks):
    if (not permalinks) or (not permalinks.strip()):
        return

    permalinks = permalinks.split('#')

    db = MySQLdb.connect(HOST_NAME,"root","","AI")

    for i in range(0, len(permalinks)):
        author = get_author(permalinks[i])
        insert_db(db, author, permalinks[i])

        print (author, permalinks[i])

    db.close()

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_POST(self):    
    print self.client_address

    form = cgi.FieldStorage(
        fp = self.rfile,
        headers = self.headers,
        environ = {'REQUEST_METHOD':'POST',
        'CONTENT_TYPE':self.headers['Content-Type'],
        })

    dump_data(form["links"].value)

    self.send_response(200)

if __name__ == '__main__':
  server_class = BaseHTTPServer.HTTPServer
  httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
  
  print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  httpd.server_close()

  print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)
