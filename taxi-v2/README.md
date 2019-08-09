# OpenAI Gym's Taxi-v2 task

My solution for the OpenAI Gym's Taxi-v2 task

## Try it yourself
The main implementation of different algorithms can be found in agent.py

Use the main.py script file to run the training

```bash
$ python main.py
Episode 20000/20000 || Best average reward 9.062

[+] Best Avg Reward:  9.06
```

## Experimentations
Here I list the best average reward I got while trying different algorithms

#### Decayed Epsilon
- Sarsamax (alpha=.1, gamma=1.0, epsilon=1.0, eps_decay=0.999, eps_min=0.1) => 5.43
- Sarsa (alpha=.1, gamma=1.0, epsilon=1.0, eps_decay=0.999, eps_min=0.1) => 6.23
- Expected Sarsa (alpha=.1, gamma=1.0, epsilon=1.0, eps_decay=0.999, eps_min=0.1) => 5.17

#### Fixed Epsilon
- Sarsamax (alpha=.1, gamma=1.0, epsilon=0.005) => 9.09
- Sarsa (alpha=.1, gamma=1.0, epsilon=0.005) => 9.27
- Expected Sarsa (alpha=.1, gamma=1.0, epsilon=0.005) => 9.35
