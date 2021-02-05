# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:54:37 2021

@author: USER
"""
setBlocks(x-2,y-1,z-2,x+2,y-1,z+2,4)

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

a=0

while a < 10:
    mc.setBlocks(x-30,y-1,z,x+30,y-1,z,19)
    z=z+5
    a=a+1