'''
Author: JIANG Yilun
Date: 2021-11-30 23:06:17
LastEditTime: 2021-11-30 23:06:17
LastEditors: JIANG Yilun
Description: 
FilePath: /INF_101/INF101/TP/Projet Final/generation.py
'''
import numpy as np
import pandas as pd

from itertools import product
from functools import reduce

ACTIONLIST = {
    0: 'skip',
    1: 'draw'
}

CARDS = np.array([2,3,4,5,6,7,8,9,10,10,10,10,11])
BLACKJACK = 21
DEALER_SKIP = 17
STARTING_CARDS_PLAYER = 2
STARTING_CARDS_DEALER = 1

STATELIST = {0: (0,0,0)} # Game start state
STATELIST = {**STATELIST, **{nr+1:state for nr, state in enumerate(product(range(2), range(CARDS.min()*STARTING_CARDS_PLAYER,BLACKJACK + 2), range(CARDS.min()*STARTING_CARDS_DEALER, BLACKJACK+2)))}}


def cartesian(x,y):
    return np.dstack(np.meshgrid(x, y)).reshape(-1, 2).sum(axis=1)


def deal_card_probability(count_now, count_next, take=1):
    if take > 1:
        cards = reduce(cartesian, [CARDS]*take)
    else:
        cards = CARDS
        
    return (np.minimum(count_now + cards, BLACKJACK + 1) == count_next).sum() / len(cards)


def is_gameover(skipped, player, dealer):
    return any([
        dealer >= DEALER_SKIP and skipped == 1,
        dealer > BLACKJACK and skipped == 1,
        player > BLACKJACK
     ])

def blackjack_probability(action, stateid_now, stateid_next):
    skipped_now, player_now, dealer_now  = STATELIST[stateid_now]
    skipped_next, player_next, dealer_next = STATELIST[stateid_next]
    
    if stateid_now == stateid_next:
        # Game cannot stay in current state
        return 0.0
    
    if stateid_now == 0:
        if skipped_next == 1:
            # After start of the game the game cannot be in a skipped state
            return 0
        else:
            # State lower or equal than 1 is a start of a new game
            dealer_prob = deal_card_probability(0, dealer_next, take=STARTING_CARDS_DEALER)
            player_prob = deal_card_probability(0, player_next, take=STARTING_CARDS_PLAYER)

            return dealer_prob * player_prob
    
    if is_gameover(skipped_now, player_now, dealer_now):
        # We arrived at end state, now reset game
        return 1.0 if stateid_next == 0 else 0.0
    
    if skipped_now == 1:
        if skipped_next == 0 or player_next != player_now:
            # Once you skip you keep on skipping in blackjack
            # Also player cards cannot increase once in a skipped state
            return 0.0
    
    if ACTIONLIST[action] == 'skip' or skipped_now == 1:
        # If willingly skipped or in forced skip (attempted draw in already skipped game):
        if skipped_next != 1 or player_now != player_next:
            # Next state must be a skipped state with same card count for player
            return 0.0
    
    if ACTIONLIST[action] == 'draw' and skipped_now == 0 and skipped_next != 0:
        # Next state must be a drawable state
        return 0.0
    
    if dealer_now != dealer_next and player_now != player_next:
        # Only the player or the dealer can draw a card. Not both simultaneously!
        return 0.0

    # Now either the dealer or the player draws a card
    if ACTIONLIST[action] == 'draw' and skipped_now == 0:
        # Player draws a card
        prob = deal_card_probability(player_now, player_next, take=1)
    else:
        # Dealer draws a card
        if dealer_now >= DEALER_SKIP:
            if dealer_now != dealer_next:
                # Dealer always stands once it has a card count higher than set amount
                return 0.0
            else:
                # Dealer stands
                return 1.0

        prob = deal_card_probability(dealer_now, dealer_next, take=1)

    return prob


def blackjack_rewards(action, stateid):
    skipped, player, dealer  = STATELIST[stateid]
    
    if not is_gameover(skipped, player, dealer):
        return 0
    elif player > BLACKJACK or (player <= dealer and dealer <= BLACKJACK):
        return -1
    elif player == BLACKJACK and dealer < BLACKJACK:
        return 1.5
    elif player > dealer or dealer > BLACKJACK:
        return 1
    else:
        raise Exception(f'Undefined reward: {skipped}, {player}, {dealer}')
    
    
# Define transition matrix
T = np.zeros((len(ACTIONLIST), len(STATELIST), len(STATELIST)))
for a, i, j in product(ACTIONLIST.keys(), STATELIST.keys(), STATELIST.keys()):
    T[a,i,j] = blackjack_probability(a, i, j)
    
# Define reward matrix
R = np.zeros((len(STATELIST), len(ACTIONLIST)))
for a, s in product(ACTIONLIST.keys(), STATELIST.keys()):
    R[s, a] = blackjack_rewards(a, s)
    

def print_blackjack_policy(policy):
    idx = pd.MultiIndex.from_tuples(list(STATELIST.values()), names=['Skipped', 'Player', 'Dealer'])
    S = pd.Series(['x' if i == 1 else '.' for i in policy], index=idx)
    S = S.loc[S.index.get_level_values('Skipped')==0].reset_index('Skipped', drop=True)
    S = S.loc[S.index.get_level_values('Player')>0]
    S = S.loc[S.index.get_level_values('Dealer')>0]
    return S.unstack(-1)

def print_blackjack_rewards():
    idx = pd.MultiIndex.from_tuples(list(STATELIST.values()), names=['Skipped', 'Player', 'Dealer'])
    S = pd.Series(R[:,0], index=idx)
    S = S.loc[S.index.get_level_values('Skipped')==1].reset_index('Skipped', drop=True)
    S = S.loc[S.index.get_level_values('Player')>0]
    S = S.loc[S.index.get_level_values('Dealer')>0]
    return S.unstack(-1)

# Check that we have a valid transition matrix with transition probabilities summing to 1
assert (T.sum(axis=2).round(10) == 1).all()