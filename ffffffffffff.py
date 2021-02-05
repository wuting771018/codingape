# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 11:17:01 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
import time 
import random
mc=Minecraft.create()
 fower=38True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,fower)
    time.sleep(0.2)