import pymysql

class MariaDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='ubuntu', password='1234567890', db='shopping_db')
        self.cur = self.db.cursor()
        print("connect ok")

    def add(self, temp, hum):
        sql = "insert into record_dht(temperature, humidity) values('{0}', '{1}')".format(temp, hum)
        self.cur.execute(sql)
        self.db.commit()
        return [temp, hum]
    
    def selectAll(self):
        sql = "select * from record_dht"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result