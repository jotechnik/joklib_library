#Copyright 2020 Jan-Ole G. (J-O. Technik)
#This example creates a Table in your database.
from joklib import database

db = database('yourDatabase.db')
db.createtable('yourTable', "'yourcoulumnName' yourcoulumnType, 'yourcoulumnName' yourcoulumnType, 'yourcoulumnName' yourcoulumnType")
db.close()