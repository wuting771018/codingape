# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:59:38 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
color=random.randrange(0,16)
mc.seeBlocks(x-25,y-1,z+25,y-1,x+25,95,color)
while True:
mc.seeBlocks(x+5,y-1,z+5,x-5,y-1,z-5,95,color)
    color=randon.randint(0,16)
    time.sleep(0.5)
