# Navigation

The goal for this project is to train an agent to navigate and collect bananas in a large, square world.

![banana-environment](imgs/banana-env.gif)

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

- `0` - move forward
- `1` - move backward
- `2` - move left
- `3` - move right

The environment is considered solved when the agent get an average score of +13 over 100 consecutive episodes.

## Setup the environment

You will first need to download the environment, just select the environment that matches your operating system:

- Linux: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): click [here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

You can then unzip it along with this project's repository under navigation to work with the provided python notebook.

Then please follow the instructions found [here](https://github.com/udacity/deep-reinforcement-learning#dependencies) to install the dependencies.

## Training

The `model.py` already contains a model that was able to solve the problem, however, you can also tweak it and rerun the notebook to check the results. You can also update the training loop in the `Navigation.ipynb` or the agent in `dqn_agent.py`. Please check the report [here](/report.md) for more details about the algorithm used.
