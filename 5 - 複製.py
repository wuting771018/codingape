# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 11:59:49 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()


for i in range(20):
    mc.set Block(x+i,y-1,z+i,4)
    mc.setBlock(x+i-1,y-1,z+i,4)
    mc.setBlock(x+i+1,y-1,z+i,4)
