# Task1_Gym-lib_BCR
First task for Behavioural and Cognitive Robotics Course.
* For the practical task about familiarizing with AI-Gym commands by using the “Cartpole-v0” environment, a python script is attached to this repo that evaluate the agent (that move by performing random actions, for 10 episodes) and which compute the fitness, i.e. the sum of the reward received every step.
* For the theoritical task about understanding one of the classical control problems ( obsvertion vector, action vector, reset function, calculation of the reward and termination criteria)
## Name: MountainCar-v0  
* Category: Classic Control
* Description: Get an under powered car to the top of a hill (top = 0.5 position)

### Observation

Type: Box(2)

Num | Observation  | Min  | Max  
----|--------------|------|----   
0   | position     | -1.2 | 0.6
1   | velocity     | -0.07| 0.07


### Actions

Type: Discrete(3)

Num | Action|
----|-------------|
0   | push left   |
1   | no push     |
2   | push right  |

### Reward

-1 for each time step, until the goal position of 0.5 is reached. As with MountainCarContinuous v0, there is no penalty for climbing the left hill, which upon reached acts as a wall.

### Starting State

Random position from -0.6 to -0.4 with no velocity.

### Episode Termination

The episode ends when you reach 0.5 position, or if 200 iterations are reached.
