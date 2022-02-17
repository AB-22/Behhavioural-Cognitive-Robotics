import gym

env = gym.make('CartPole-v0')
# to calculate the total reward of all episodes
reward_avg = 0
for i_episode in range(10):
    observation = env.reset()
    print("--------------------------------------------------------------")
    #To calculate the reward of each episode
    episode_reward = 0
    for t in range(100):
        env.render()
        print("observation {}: {}".format(t, observation))
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print("timestep {}, reward = {}".format(t, reward))
        episode_reward += reward
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
    reward_avg += episode_reward
    print("average reward", reward_avg)
    print("episode {}, reward = {}".format(i_episode, episode_reward))

env.close()
