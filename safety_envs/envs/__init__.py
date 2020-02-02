from safety_gym.envs.engine import Engine
from gym.envs.registration import register

"""
Environments obtained from safety-gym
"""
#Basic point robot environment
seed = 42
config = {# 'observation_flatten': False,
                   'robot_base': 'xmls/point.xml',
                   'observe_goal_comp': True,
                   '_seed': seed
    }

register(id='PointReach-v0',
         entry_point='safety_gym.envs.mujoco:Engine',
         kwargs={'config': config})


"""
Wrapped environments
"""
#Reach task for point robot with reduced state
register(id='BasicReach-v0',
         entry_point='safety_envs.envs.basic_reach:BasicReach')

register(id='FaultyReach-v0',
         entry_point='safety_envs.envs.faulty_reach:FaultyReach')