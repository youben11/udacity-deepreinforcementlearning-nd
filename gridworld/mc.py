"""First visit Monte Carlo prediction"""

import grid_world
import numpy as np



def run_equiprobable(gw):
    gw.reset()
    done = False
    states = []
    actions = []
    rewards = []
    while not done:
        action = np.random.choice(gw.ACTIONS)
        states.append(gw.state)
        actions.append(action)
        state, reward, done = gw.move(action)
        rewards.append(reward)
    return states, actions, rewards


def first_visit_mc(num_episodes):
    gw = grid_world.GridWorld()
    N = np.zeros((len(gw.STATES), len(gw.ACTIONS)))
    returns = np.zeros((len(gw.STATES), len(gw.ACTIONS)))
    for ep in range(num_episodes):
        states, actions, rewards = run_equiprobable(gw)
        N_at_start = N.copy()
        for t in range(len(states)):
            s = states[t]
            a = actions[t]
            gt = sum(rewards[t:])
            if N_at_start[s, a] == N[s, a]:
                N[s, a] += 1
                returns[s, a] += gt

    Q = returns / N
    return Q


def derive_policy(Q):
    states_str = grid_world.GridWorld.STATES_STR
    action_str = grid_world.GridWorld.ACTIONS_STR
    for i in range(Q.shape[0]):
        action_idx = Q[i].argmax()
        print("\t[+] %s ---> %s" % (states_str[i], action_str[action_idx]))
    return


if __name__ == '__main__':
    Q = first_visit_mc(num_episodes=100)
    print("[*] Learned Policy:")
    derive_policy(Q)
