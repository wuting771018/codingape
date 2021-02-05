# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:21:22 2021

@author: USER
"""

from  mcpi.minecraft import Minecraft  
mc=Minecraft.create()
x=248,857
y=76.0
z=255.678    
mc.player.setPos(x,y,z)