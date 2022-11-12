import gym
from gym.utils.play import play
env = gym.make("LunarLander-v2", render_mode="human")
play(env, zoom=3)

observation, info = env.reset(seed=42)

# for _ in range(1000):
   # action = policy(observation)  # User-defined policy function
   # observation, reward, terminated, truncated, info = env.step(action)

for _ in range(1000):
   observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
   if terminated or truncated:
      observation, info = env.reset()
env.close()

