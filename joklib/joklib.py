#######################joklib Library for J-O. Techniks "Klimaboxen"#######################
#This Library allows accsess to the "Klimaboxen" from J-O. Technik via the JSON HTTP request from the Server
#and also some basic other functions for IoT.
#Copyright 2020 Jan-Ole G. (J-O. Technik)

#This library uses two other librarys to work. First the Python requestes Library: https://pypi.org/project/requests/
#And second the Python sqlite3 Library.
import requests
import sqlite3

class klimbox:
    def __init__(self, hostaddr, hostpor):
        self.hostaddress = hostaddr
        self.hostport = hostpor
        response = requests.get(hostaddr+':'+str(hostpor)+'/json/d00')
        self.durchschnitt = str(response.json())
        self.gestemp = self.durchschnitt[9:14]
        self.geshum = self.durchschnitt[16:21]
        self.gespress = self.durchschnitt[23:32]
        self.gestimestamp = self.durchschnitt[35:54]
        self.gesdate = self.gestimestamp[0:10]
        self.gestime = self.gestimestamp[11:19]
    def boxin(self, boxinitial='d00', boxprot='wifi'):
        response = requests.get(self.hostaddress+':'+str(self.hostport)+'/json/'+boxinitial)
        self.data = str(response.json())
        self.boxprotokol = boxprot
        if(self.boxprotokol == 'wifi'):
            self.temp = self.data[9:14]
            self.hum = self.data[16:21]
            self.press = self.data[23:32]
            self.timestamp = self.data[35:54]
            self.date = self.timestamp[0:10]
            self.time = self.timestamp[11:19]
        elif(self.boxprotokol == 'lora'):            
            self.temp = self.data[9:18]
            self.hum = self.data[20:29]
            self.press = self.data[31:42]
            self.timestamp = self.data[45:64]
            self.date = self.timestamp[0:10]
            self.time = self.timestamp[11:19]
        else:
            print('Protokol is not supported jet!')
            return 1;
    def printall(self):
        print("Temperature:", self.temp, "°C")
        print("Humidity:", self.hum, "%")
        print("Pressure:", self.press, "Pa")
        print("Date:", self.date)
        print("Time:", self.time)
        
class database:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
    def readalldb(self, table):
        self.cursor.execute("SELECT * FROM " + str(table))
        self.buff = self.cursor.fetchall()
        self.data = self.buff
        self.conn.commit()
    def readlastdb(self, table):
        self.counter = 1
        self.cursor.execute("SELECT * FROM " +str(table))
        self.buff = self.cursor.fetchall()
        for i in self.buff:
            if(self.counter == len(self.buff)):
                self.out = i    
            self.counter += 1
        self.data = self.out
        self.conn.commit()
    def createtable(self, name, values):
        self.cursor.execute("CREATE TABLE '"+name+"' ("+values+");")
        self.conn.commit()
    def insertintable(self, table, data):
        self.cursor.execute("INSERT INTO "+table+" VALUES ("+data+")")
        conn.commit()
    def close(self):
        self.conn.close()
        
class stdio:
    def sage(self, data):
        print(data)
    def frage(self, data):
        print(data)
        eingabe = input()
        return eingabe;