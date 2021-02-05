# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:59:57 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

x,y,z=x,y,z=mc.player.getTilePos()
for i in range(16):
 mc.setBlock(x+i,y,z,35,i)
