# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 10:44:46 2021

@author: USER
"""
from mcpi.minecraft import Minecraft 
import time 
import random


mc= Minecraft.create()


x,y,z=mc.player.getTilePos()
A=10
B=10
C=10
block=4
air=0
setBloc
mc.ks(x,y,z,x+A,y+B,z+C,block)
mc.setBlocks(x+1,y+1,z+1,x+A-1,y+B-1,z+C-1,air)