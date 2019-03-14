from project.config.sqlite import * 
import datetime

class Messaging:
    
    def getMessages(self):
	    db = database_con()
	    cur = db.execute('SELECT messageId, name, message, link, timestamp FROM messages')
	    return cur.fetchall()

    def storeMessages(self, name, message, link):
	    db = database_con()
	    cur = db.execute(''' INSERT INTO messages(name, message, link, timestamp)VALUES(?,?,?,?)''',(name, message, link, "2019" ))
	    return db.commit()
    
