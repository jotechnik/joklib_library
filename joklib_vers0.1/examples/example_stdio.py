#Copyright 2020 Jan-Ole G. (J-O. Technik)
#This example demonstrates the stdio class of the joklib library.
from joklib import stdio

io = stdio()
io.sage("Hallo Welt!!!")
ein = io.frage("Wie geht es dir???")
io.sage("Dir geht es: "+ein)