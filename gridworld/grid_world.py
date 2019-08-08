from random import random

class GridWorld(object):
    UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
    ACTIONS = [UP, RIGHT, DOWN, LEFT]
    # LEFT DOWN, LEFT UP, RIGHT UP, RIGHT DOWN
    LD, LU, RU, RD = 0, 1, 2, 3
    STATES = [LD, LU, RU]
    FINAL_STATES = [RD]

    # First index: state
    # Second index: action
    # Third index: ending at state
    # Ex: PROB[LD][UP][LU] is the probability of ending at state LU while going
    # UP at state LD
    PROBS = {
        LD: {
            UP: {LD: 0.3, LU: 0.7},
            RIGHT: {LD: 0.9, LU: 0.1},
            DOWN: {LD: 0.9, LU: 0.1},
            LEFT: {LD: 0.9, LU: 0.1},
        },
        LU: {
            UP: {LD: 0.1, LU: 0.8, RU: 0.1},
            RIGHT: {LD: 0.1, LU: 0.2, RU: 0.7},
            DOWN: {LD: 0.7, LU: 0.2, RU: 0.1},
            LEFT: {LD: 0.1, LU: 0.8, RU: 0.1},
        },
        RU: {
            UP: {LU: 0.1, RU: 0.8, RD: 0.1},
            RIGHT: {LU: 0.1, RU: 0.8, RD: 0.1},
            DOWN: {LU: 0.1, RU: 0.2, RD: 0.7},
            LEFT: {LU: 0.7, RU: 0.2, RD: 0.1},
        },
    }
    # First index: current state
    # Second index: next state
    # Ex: REWARDS[LD][LU] is the reward for moving from LD to LU
    REWARDS = {
        LD: {LD: -1, LU: -1},
        LU: {LD: -1, LU: -1, RU: -1},
        RU: {LU: -1, RU: -1, RD: 10},
    }

    def __init__(self):
        #self._check_probs()
        self.state = self.LD


    def reset(self):
        self.state = self.LD


    def _check_probs(self):
        probs_good = True
        for s in self.STATES:
            for a in self.ACTIONS:
                probs = self.PROBS[s][a].values()
                print("[*] Checking state %d with action %d" % (s, a))
                # might not sum to exactly 1 (Python precision)
                if abs(sum(probs) - 1) > 0.001:
                    print("[-] Warning: probabilities doesn't sum to 1")
                    print(self.PROBS[s][a].values())
                    print(sum(self.PROBS[s][a].values()))
                    probs_good = False
        return probs_good


    def get_next_state(self, action):
        probs = self.PROBS[self.state][action].copy()
        possible_states = probs.keys()
        cummulative_probs = 0
        # Choose the next state according to probs
        rand = random()
        for ps in possible_states:
            probs[ps] += cummulative_probs
            cummulative_probs = probs[ps]
            if rand < probs[ps]:
                return ps


    def move(self, action):
        current_state = self.state
        next_state = self.get_next_state(action)
        reward = self.REWARDS[current_state][next_state]
        is_done = next_state in self.FINAL_STATES
        self.state = next_state
        return next_state, reward, is_done


    def __str__(self):
        state = self.state
        str_states = ['LEFT_DOWN', 'LEFT_UP', 'RIGHT_UP', 'RIGHT_DOWN']
        return "State: " + str_states[state]
