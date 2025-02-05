import gymnasium as gym
from stable_baselines3 import PPO
model = PPO('MlpPolicy', gym.make('CartPole-v1', render_mode='rgb_array'), verbose=1)
model.learn(total_timesteps=1000)
vec_env = model.get_env()
obs = vec_env.reset()
for i in range(1000):
    action, _ = model.predict(obs, deterministic=True)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render('human')