# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:37:02 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
import time 
import random
mc=Minecraft.create()

count=0
fower=38

while count<50:
    x,y,z=mc.player.getTilePos()
    color=random.randrange(0,9)
    mc.setBlock(x,y,z,fower,count)
   time.sleep(0.2)
    count=count+1