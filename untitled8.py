# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:16:31 2021

@author: USER
"""

from mcpi.minecraft import Minecraft  
import time
mc=Minecraft.create()
time.sleep(5)
x=-13
y=16
z=8
mc.player.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.piayer.setTilePos(x,y,z)
time.sleep(0.5)
y=y+1
mc.player.setTilePos(x,y,z)