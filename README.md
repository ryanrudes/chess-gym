# OpenAI Gym Chess
Gym Chess is an environment for reinforcement learning with the OpenAI gym module.

<a href="https://imgbb.com/"><img src="https://i.ibb.co/Fw4fhzK/Screen-Shot-2020-10-27-at-2-30-21-PM.png" alt="Screen-Shot-2020-10-27-at-2-30-21-PM" border="0"></a>

## Installation

1. Install [OpenAI Gym](https://github.com/openai/gym) and its dependencies. \
`pip install gym`

2. Download and install `gym-chess`: \
`git clone https://github.com/Ryan-Rudes/gym-chess.git` \
`cd gym-chess` \
`python setup.py install`

## Example
```python
import gym
import gym_chess

env = gym.make("Chess-v0")

terminal = False
observation = env.reset()
while not terminal:
  action = env.action_space.sample()
  observation, reward, terminal, info = env.step(action)
  env.render()
  
env.close()
```
