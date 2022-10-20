import gym
from gym.utils.play import PlayPlot
import numpy as np
from gym.utils.play import play
env = gym.make("ALE/Asteroids-v5", render_mode='human')

env.reset()

for _ in range(100):
    env.step(env.action_space.sample())

frame_collection = env.render()
env.close()


# def callback(obs_t, obs_tp1, action, rew, terminated, truncated, info):
#    return [rew, ]
#
# plotter = PlayPlot(callback, 150, ["reward"])
# play(gym.make("ALE/AirRaid-v5"), callback=plotter.callback)

# play(env, zoom=3, fps=60)


# observation, info = env.reset(seed=42)
#
# # for _ in range(1000):
#    # action = policy(observation)  # User-defined policy function
#    # observation, reward, terminated, truncated, info = env.step(action)
#
# for _ in range(1000):
#    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
#    if terminated or truncated:
#       observation, info = env.reset()
# env.close()

