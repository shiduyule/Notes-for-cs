# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:46:21 2022

@author: shiduyule
"""
import matlab.engine
eng=matlab.engine.start_matlab()
a = matlab.double([1,4,9,16,25])
print(type(a))
b=eng.sqrt(a)
print(b)
for b1 in b:
    for b2 in b1:
        print(b2)
