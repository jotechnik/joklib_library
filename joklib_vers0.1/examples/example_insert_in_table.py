#Copyright 2020 Jan-Ole G. (J-O. Technik)
#This example puts dada in your table.
from joklib import database

db = database('yourDB.db')
db.insertintable('yourTable', 'yourdata')
db.close()