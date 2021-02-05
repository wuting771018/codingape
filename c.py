# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:29:17 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
import time 
import random

mc=Minecraft.create()

while True:
x,y,z=mc.player.getpos()
x=x+random.uniform(-20,20)
z=z+random.uniform(-20,20)
y=y+30
mc.(x,y,z,93)
time.sleep(0.2)

