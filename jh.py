# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:35:04 2021

@author: USER
"""


x,y,z=x,y,z=mc.player.getTilePos()

for i in range(10):
    r=random.randrange(1,5)
    if r==1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
    elif r==2:
        x=x+4   
        mc.setBlocks(x,y,z,x-4,y,z,1)
    elif r==3:
        x=x-4 
        mc.setBlocks(x,y,z,x,y,z+4,1)
        z=z+4
    elif r==4:
        mc.setBlocks(x,y,z,x,y,z-4,1)
        z=z-4