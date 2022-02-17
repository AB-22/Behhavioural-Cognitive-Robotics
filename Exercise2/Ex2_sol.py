import time
import gym
import numpy as np
from numpy.core.defchararray import count


class Network:

    def __init__(self,env):


        self.cumreward =[]
        self.pvariance = 0.1     # variance of initial parameters
        self.ppvariance = 0.02   # variance of perturbations
        self.nhiddens = 5        # number of internal neurons
        # the number of inputs and outputs depends on the problem
        # we assume that observations consist of vectors of continuous value
        # and that actions can be vectors of continuous values or discrete actions
        self.ninputs = env.observation_space.shape[0]
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            self.noutputs = env.action_space.shape[0]
        else:
            self.noutputs = env.action_space.n

    def initparameters(self):
        # initialize the training parameters randomly by using a gaussian
        # distribution with average 0.0 and variance 0.1
        # biases (thresholds) are initialized to 0.0
        self.W1 = np.random.randn(self.nhiddens,self.ninputs) * self.pvariance      # first connection layer
        self.W2 = np.random.randn(self.noutputs, self.nhiddens) * self.pvariance    # second connection layer
        self.b1 = np.zeros(shape=(self.nhiddens, 1))                      # bias internal neurons
        self.b2 = np.zeros(shape=(self.noutputs, 1))                      # bias motor neurons
        #self.env_w = [W1 , W2 ,b1 ,b2 ,self.ninputs]

    def update(self,observation):
        #W1 , W2 ,b1 ,b2 ,ninputs = self.env_w
        # change chape to be able to multiply the matrix between observation and connection and weights
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(self.ninputs,1)
        # compute the netinput of the first layer of neurons
        self.Z1 = np.dot(self.W1, observation) + self.b1
        # compute the activation of the first layer of neurons with the tanh function
        self.A1 = np.tanh(self.Z1)
        # compute the netinput of the second layer of neurons
        self.Z2 = np.dot(self.W2, self.A1) + self.b2
        # compute the activation of the second layer of neurons with the tanh function
        self.A2 = np.tanh(self.Z2)
        # if the action is discrete
        #  select the action that corresponds to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = self.A2 # if the action is integer [0 , 1]
        else:
            action = np.argmax(self.A2)  #

        return(action)

    def evaluate(self, nepisodes):
        cumreward = 0
        # self.env.render(mode = 'rgb_array')
        for e in range(nepisodes):
            observation = env.reset()
            done = False
            while not done :
                action = network.update(observation)
                observation, reward, done, info = env.step(action)
                cumreward += reward


        return cumreward/nepisodes

    def render(self, nepisodes):

        for e in range(nepisodes):
            self.cumreward =[]
            observation = env.reset()
            done = False
            while not done :
                env.render()
                action = network.update(observation)
                observation, reward, done, info = env.step(action)
                self.cumreward.append(reward)
                time.sleep(0.05)
                print(sum(self.cumreward))
        env.close()
        return reward


env=gym.make('CartPole-v0')
network= Network(env)
network.initparameters()
fitness = network.evaluate(3) # 3 is number of episods
print("_____________________________Done!______________________________")

network.render(3)
