# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 18:43:02 2021

This script aims to show some method of the class numpy

@author: Andrea Pasqua
"""

import numpy as np
import math

# Create arrays with int or float
myArray1 = np.array([2,3,4])
myArray2 = np.array([2.3, 6.4, 89.0])
# Create some "special" arrays (zeros, ones, empty)
arrayZero = np.zeros((5,5))
arrayOnes = np.ones((5,5))
arrayNull = np.empty((5,5))
# Define the arrays type
typeMyArray1 = myArray1.dtype
typeMyArray2 = myArray2.dtype
typeArrayZero = arrayZero.dtype
typeArrayOnes = arrayOnes.dtype
typeArrayNull = arrayNull.dtype

# Print the arrays and their type
print(myArray1,typeMyArray1)
print(myArray2,typeMyArray2)
print(arrayZero,typeArrayZero)
print(arrayOnes,typeArrayOnes)
print(arrayNull,typeArrayNull)

# Create an arrays of arrays
myArrayArray1 = np.array([(1.5,2,3), (4,5,6)])
print(myArrayArray1)

# uses arange instead of range for numpy library
myFirstSerie = np.arange(15).reshape(3,5) #reshape the vector
mySecondSerie = np.arange(0, 2, 0.3).ndim # calculate the dimensions
myTirthSerie = np.linspace(0,2*math.pi,100) # generate linearly spaced vector

#  Convert myTirthSerie in degs
degList = []
for i in range(myTirthSerie.size):
    degVal = math.degrees(myTirthSerie[i])
    degList.append(degVal)
    