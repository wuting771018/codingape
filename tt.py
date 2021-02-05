# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:55:20 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

number=1
x,y,z=x,y,z=mc.player.getTilePos()

for i in range(8):
    for j in range(number):
        mc.spawnEntity(x,y,z,60)
        
        
        
    number=2*number
    mc.postToChat("這次生成了"+str( number)+"隻蠧魚")
    time.sleep(1)      
