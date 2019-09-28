# Continuous Control

![reacher-environment](imgs/reacher.gif)

In this environment, a double-jointed arm can move to target locations. A reward of +0.1 is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between -1 and 1.

This project train on 20 parallel double-joined arm and is considered solved when the agent get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,

- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 20 (potentially different) scores. We then take the average of these 20 scores.

- This yields an average score for each episode (where the average is over all 20 agents).

## Setup the environment

You will first need to download the environment, just select the environment that matches your operating system:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)

You can then unzip it along with this project's repository under continuous_control to work with the provided python notebook.

Then please follow the instructions found [here](https://github.com/udacity/deep-reinforcement-learning#dependencies) to install the dependencies.

## Training

The `model.py` already contains a model that was able to solve the problem, however, you can also tweak it and rerun the notebook to check the results. You can also update the training loop in the `Continuous_Control.ipynb` or the agent in `ddpg_agent.py`. Please check the report [here](./report.md) for more details about the algorithm used.
