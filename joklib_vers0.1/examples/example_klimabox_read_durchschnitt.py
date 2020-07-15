#Copyright 2020 Jan-Ole G. (J-O. Technik)
#In this example data is read from the database and print out on the screen.
from joklib import klimbox

box = klimbox('http://yourHost', 80)
box.boxin('yourRoomTable', 'wifi')
print(box.data)