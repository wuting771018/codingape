# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 15:18:40 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
mc=Minecraft.create("I m watching you.")
while True:
   x,y,z=mc.player.getTilePos()
   mc.postToChat("You are located on x:"+str(x)+",Y:"+str(y)+",z:"+str(z))
    
