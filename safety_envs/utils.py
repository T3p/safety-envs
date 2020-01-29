#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:32:59 2020

@author: matteo
"""
import numpy as np

def filter_ob(ob, mask):
    return np.array([o for o, i in zip(ob, mask) if i])