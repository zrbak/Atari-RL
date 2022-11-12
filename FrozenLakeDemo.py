import gym
from gym.utils.save_video import save_video
env = gym.make("FrozenLake-v1", render_mode="human")
env.reset()
step_starting_index = 0
episode_index = 0
for step_index in range(199):
   action = env.action_space.sample()
   _, _, done, _ = env.step(action)
   if done:
      save_video(
         env.render(),
         "videos",
         fps=env.metadata["render_fps"],
         step_starting_index=step_starting_index,
         episode_index=episode_index
      )
      step_starting_index = step_index + 1
      episode_index += 1
      env.reset()
env.close()