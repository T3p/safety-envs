#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:47 2020

@author: matteo

Wraps the basic safety-gym point-robot task reducing its state

"""

import gym
import safety_envs.envs
from safety_envs.utils import filter_ob


class BasicReach(gym.Env):

  def __init__(self):
    self.wrapped = gym.make('PointReach-v0')
    self.mask = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]  
    
  def step(self, action):
    ob, reward, done, info = self.wrapped.step(action)
    ob = filter_ob(ob, self.mask)
    return ob, reward, done, info
      
  def reset(self):
    ob = self.wrapped.reset()
    return filter_ob(ob, self.mask)

  def render(self, mode='human'):
    return self.wrapped.render(mode=mode)

  def close(self):
    return self.wrapped.close()
