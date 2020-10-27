# OpenAI Gym Chess
Gym Chess is an environment for reinforcement learning with the OpenAI gym module.

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
