# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:53:09 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 

mc=Minecraft.create()

while True:
    hits=mc.events. pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.z
        mc.setBlockhits()