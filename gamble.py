import math
import random
import numpy as np

# orba gain every 5 steps
orba_gain = 29

# plug in current orba
current_orba = 49332

# place a bet and randomly update
def update(orba_, bet_):
    a = random.random()
    if a<0.5:
        gain = 0-bet_
        win = False
    elif a<0.99:
        gain = bet_
        win = True
    else:
        gain = 2*bet_
        win = True
    return orba_+gain, win

# monte carlo sims
num_sims = 10000
num_steps = 1000
best_strat = None
best_gain = 0
# run sims for martingale strategy
for k in range(1, 21):
    gains = []
    for _ in range(num_sims):
        orba = current_orba
        start = True
        prev_bet = 0
        for n in range(num_steps):
            if start:
                prev_bet = math.floor(current_orba/(2.0**k-1))
                bet = prev_bet
            else:
                bet = prev_bet*2
                prev_bet = bet
            if bet>orba:
                prev_bet = math.floor(current_orba/(2.0**k-1))
                bet = prev_bet
            orba, win = update(orba, bet)
            if n%5==0:
                orba+=orba_gain
            start=win

        gain = orba-current_orba
        gains.append(gain)

    gains = np.array(gains)
    avg_gain = np.mean(gains)
    var_gain = np.var(gains)

    print("martingale_"+str(k))
    print(avg_gain)
    print(var_gain)
    print("******************************************************")
    if avg_gain>best_gain:
        best_gain = avg_gain
        best_strat = "martingale_"+str(k)

print(best_strat)
print(best_gain)