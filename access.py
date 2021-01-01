import threading
import time
import datastore as x 

x.create_key("Christy",100)
print()
x.create_key("Python",70,1200) 
print()
x.read_value("Christy")
print()
x.read_value("Python")
print()
x.create_key("Christy",50)
print()
x.modify_value("Christy",55)
print()
x.read_value("Christy")
print()
x.delete_key("Christy")

t1=threading.Thread()
t1.start()
time.sleep(10)
