# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:17:49 2021

@author: USER
"""

from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

list1=[]
list2=[]
list3=[]
for i in range(1,4):
  list1.append(1*i)
  list2.append(2*i)
  list3.append(3*i)
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,str(list1),)
