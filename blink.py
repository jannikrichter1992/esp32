# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 14:04:59 2020

@author: Jannik
"""

import machine
import time

x = int
y = int

x = 7
y = 7

p = machine.Pin(1, machine.Pin.OUT)

p.value(1)
if x == y:
    p.value(0)
    time.sleep(1)
    p.value(1)
    time.sleep(1)
    p.value(0)
    time.sleep(1)
    p.value(1)
    
else:
    p.value(1)