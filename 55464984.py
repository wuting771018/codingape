# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 16:15:08 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
y=y-1
mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,11)


