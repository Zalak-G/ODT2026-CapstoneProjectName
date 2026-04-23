from machine import Pin
import neopixel
import random
import time

np1 = neopixel.NeoPixel(Pin(23),16)
np2 = neopixel.NeoPixel(Pin(5),16)
np3 = neopixel.NeoPixel(Pin,(x),16)

while True:
    for i in range(0, 16):
        # Set first neopixel to RED, second neopixel to GREEN, and third neopixel to BLUE
        np1[i] = (255, 0, 0)
        np2[i] = (0, 255, 0)
        np3[i] = (0, 0, 255)
    
    r_npx = random.randint(1,3)
    print (r_npx)
    time.sleep(10)
    
        if r_npx == 1:
            np1.write()
            np2[i] = (0, 0, 0)
            np3[i] = (0, 0, 0)
            
        elif r_npx == 2:
            np2.write()
            np1[i] = (0, 0, 0)
            np3[i] = (0, 0, 0)
            
        elif r_npz == 3:
            np3.write()
            np1[i] = (0, 0, 0)
            np2[i] = (0, 0, 0)
        
    time.sleep(10)
    
      for i in range(0, 16):
        # Turn all neopixels off
        np1[i] = (0, 0, 0)
        np2[i] = (0, 0, 0)
        np3[i] = (0, 0, 0)
        
    time.sleep(10)