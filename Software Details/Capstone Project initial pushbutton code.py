from machine import Pin
import time

pba = Pin(x,Pin.IN,Pin.PULL_UP)
pbb = Pin(x,Pin.IN,Pin.PULL_UP)
pbc = Pin(x,Pin.IN,Pin.PULL_UP)
pbd = Pin(x,Pin.IN,Pin.PULL_UP)

while true:
    
    val_a = pba.value()
    val_b = pbb.value()
    val_c = pbc.value()
    val_d = pbd.value()
    
    if val_a == 0:
        print("Button A is pressed")
        
    elif val_b == 0:
        print("Button B is pressed")
        
    elif val_c == 0:
        print("Button C is pressed")
        
    elif val_d == 0:
        print("Button D is pressed")
        
        
    time.sleep(0.5)
        
        
        
        