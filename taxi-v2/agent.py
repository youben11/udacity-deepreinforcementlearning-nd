import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6, alpha=.1, gamma=1.0, epsilon=0.005, eps_decay=0.99999, eps_min=0.1):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.alpha = alpha
        self.gamma = gamma
        self.eps = epsilon
        self.eps_decay = eps_decay
        self.eps_min = eps_min

        self.states = []
        self.actions = []
        self.rewards = []


    def select_action(self, state):
        """ Given the state, select an action
            following an e-greedy policy.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """

        probs = np.ones(self.nA) * (self.eps / self.nA)
        greedy_action = self.Q[state].argmax()
        probs[greedy_action] += 1 - self.eps
        action = np.random.choice(self.nA, p=probs)
        return action

    def update_eps(self):
        self.eps = max(self.eps * self.eps_decay, self.eps_min)

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        self.update_Q_expected(state, action, reward, next_state, done)

    def update_Q_mc_control(self, state, action, reward, next_state, done):
        self.states.append(state)
        self.actions.append(action)
        self.rewards.append(reward)

        if done:
            self.eps = 0.005
            rewards = np.array(self.rewards)
            discounts = np.array([self.gamma ** i for i in range(len(rewards)+1)])
            for t, (s, a) in enumerate(zip(self.states, self.actions)):
                Gt = sum(rewards[t:] * discounts[:-(1+t)])
                self.Q[s][a] += self.alpha * (Gt - self.Q[s][a])

            #self.update_eps()
            # Empty saved episode
            self.states = []
            self.actions = []
            self.rewards = []


    def update_Q_sarsamax(self, state, action, reward, next_state, done):
        if done:
            self.update_eps()

        self.Q[state][action] += self.alpha * (reward + self.gamma * max(self.Q[next_state]) - self.Q[state][action])


    def update_Q_sarsa(self, state, action, reward, next_state, done):
        if done:
            self.update_eps()

        next_action = self.select_action(next_state)
        self.Q[state][action] += self.alpha * (reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action])

    def update_Q_expected(self, state, action, reward, next_state, done):
        # if done:
        #     self.update_eps()

        probs = np.ones(self.nA) * (self.eps / self.nA)
        greedy_action = self.Q[next_state].argmax()
        probs[greedy_action] += 1 - self.eps
        expected = np.dot(self.Q[next_state], probs)
        self.Q[state][action] += self.alpha * (reward + self.gamma * expected - self.Q[state][action])
