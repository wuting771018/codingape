# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:13:31 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 

mc=Minecraft.create()

x,y,z=mc.player.getpos()
mc.spawnEntity(x,y,z,93)
    
