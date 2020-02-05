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
import numpy as np
import math


def bias_compass_observation(x, y, offset):
    alpha = get_angle(x, y)
    alpha = offset_sum2(alpha, offset)
    sin_alpha, cos_alpha = get_sin_cos(alpha)
    return cos_alpha, sin_alpha

# given cos and sin return the angle in degrees
def get_angle(x, y):
    alpha_rad = np.arctan(y/x)
    alpha = 57.3 * alpha_rad
    if alpha > 0 and x < 0:  # correction arctan
        alpha += 180
    if alpha < 0 and x < 0:  # correction arctan
        alpha += 180
    if alpha < 0:  # correction neg alpha
        alpha += 360
    return alpha

def offset_sum2(angle, offset):
    angle += offset
    if angle > 360:
        angle -= 360
    return angle

def get_sin_cos(angle):
    angle = angle / 57.3
    return math.sin(angle), math.cos(angle)

class FaultyReach(gym.Env):

    def __init__(self):
        self.wrapped = gym.make('PointReach-v0')
        self.mask = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]  
        self.observation_space = gym.spaces.Box(-np.inf, np.inf, (sum(self.mask),), dtype=np.float32) 
        self.action_space = self.wrapped.action_space
        self.offset = 20
    
    def step(self, action):
        ob, reward, done, info = self.wrapped.step(action)
        ob = self.faulty_ob(ob)
        return ob, reward, done, info
      
    def reset(self):
        ob = self.wrapped.reset()
        return self.faulty_ob(ob)

    def render(self, mode='human'):
        return self.wrapped.render(mode=mode)

    def close(self):
        return self.wrapped.close()

    def seed(self, seed):
        return self.wrapped.seed(seed)

    def faulty_ob(self, obs):
        obs = filter_ob(obs, self.mask)
        # to simulate a damage in compass
        obs[2], obs[3] = bias_compass_observation(obs[2], obs[3], self.offset)
        return obs
  
