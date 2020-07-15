#Copyright 2020 Jan-Ole G. (J-O. Technik)
#This example reads data from your table.
from joklib import database

db = database('yourDB.db')
db.readlastdb('yourTable')
print(db.data)
db.close()