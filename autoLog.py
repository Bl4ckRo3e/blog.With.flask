# from models import Log, db
from datetime import datetime
import sqlite3


now = datetime.now()

class Log:
    def __init__(this, ip, work):
        this.ip = ip
        this.work = work
        this.getLog()

    def getLog(this):
        try:
            # new_log = Log(ip=this.ip, time=f'{this.now.strftime("%Y/%m/%d %H:%M:%S")}', work=this.work)
            # db.session.add(new_log)
            # db.session.commit()
            conn = sqlite3.connect('Database.db')
            cursor = conn.cursor()
            time = now.strftime("%Y/%m/%d %H:%M:%S")
            data = ( this.ip,time,  this.work)
            # Insert data into table
            cursor.execute('INSERT INTO Logs (ip,time,work) VALUES (?,?,?)', data)
            # Commit changes and close connection
            conn.commit()
            conn.close()
            print("Added")
        except Exception as e:
            print(e)