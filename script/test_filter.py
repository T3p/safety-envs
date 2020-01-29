#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:37:38 2020

@author: matteo
"""

import safety_envs
import gym

seed = 42

env1 = gym.make('PointReach-v0')
env2 = gym.make('BasicReach-v0')

print('State dim of original task:')
print('reset():', len(env1.reset()))
print('step(1):', len(env1.step(1.)[0]))

print('\nState dim of reduced task:')
print('reset():', len(env2.reset()))
print('step(1):', len(env2.step(1.)[0]))

print()
env1.seed(seed)
print(env1.reset(), '\n->')
env2.seed(seed)
print(env2.reset())

print()
env1.seed(seed)
print(env1.step(1.)[0], '\n->')
env2.seed(seed)
print(env2.step(1.)[0])
