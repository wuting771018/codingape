# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:20:17 2021

@author: USER
"""
from mcpi.minecraft import Minecraft
import time

mc = Minecraft.create()

while True:
    mc.executeCommand("time add 50")
    time.sleep(0.2)
