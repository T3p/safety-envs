#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:03:47 2020

@author: matteo

Wraps the basic safety-gym point-robot task reducing its state

"""

import gym
import safety_envs.envs


class BasicReach(gym.Env):

  def __init__(self):
    self.wrapped = gym.make('PointReach-v0')
      
  def step(self, action):
    obs, reward, done, info = self.wrapped.step(action)
    return obs, reward, done, info
      
  def reset(self):
    return self.wrapped.reset()

  def render(self, mode='human'):
    return self.wrapped.render(mode=mode)

  def close(self):
    return self.wrapped.close()
