from safety_gym.envs.engine import Engine
from gym.envs.registration import register

seed = 42

config = {# 'observation_flatten': False,
                   'robot_base': 'xmls/point.xml',
                   'observe_goal_comp': True,
                   '_seed': seed
    }

register(id='SGBasic-v0',
         entry_point='safety_gym.envs.mujoco:Engine',
         kwargs={'config': config})

