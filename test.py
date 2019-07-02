from lightblue import *
s = socket()        # or socket(L2CAP) to create an L2CAP socket
s.connect(("00:12:2c:45:8a:7b", 5))
s.send("hello")
s.close()
