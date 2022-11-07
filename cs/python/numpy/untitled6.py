# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 12:21:08 2022

@author: shiduyule
"""
import numpy as np 
a = np.array([
       [[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]],

       [[19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]]])
b = np.array([
        [ 1,  2,  3, 4],
        [ 5,  6,  7, 8],
        [ 9, 10, 11,12]])

print(b.shape)
b = b[:,None]
