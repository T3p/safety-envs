#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:37:38 2020

@author: matteo
"""

import safety_envs
import gym

env1 = gym.make('PointReach-v0')
env2 = gym.make('BasicReach-v0')

print('State dim of original task:')
print('reset:', len(env1.reset()))
print('step:', len(env1.step()))

print('\nState dim of reduced task:')
print('reset:', len(env2.reset()))
print('step:', len(env2.step()))

env1.seed(0)
env2.seed(0)

print()
print(env1.reset(), '\n->\n', env2.reset())
print()
print(env1.step(1.), '\n->\n', env2.step(1.))