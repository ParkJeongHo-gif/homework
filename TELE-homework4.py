# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:36:56 2020

@author: 박정호
"""
import turtle
class myturtle(turtle.Turtle):
    def drawsquare(self):
        for i in range(4):
            self.right(90)
            self.forward(90)
myturtle.drawsquare(turtle)
