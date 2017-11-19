# -----------
# User Instructions
# 
# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
# card_ranks(hand) returns an ORDERED tuple of the ranks 
#                  in a hand (where the order goes from
#                  highest to lowest rank). 
#
# Since we are assuming that some functions are already
# written, this code will not RUN. Clicking SUBMIT will 
# tell you if you are correct.
import random
from itertools import *


hand_names = ['Straight Flush', '4 Kind', 'Full House', 'Flush',
              'Straight', '3 Kind', '2 Pairs', 'Pair', 'High Card']


def deal(hands_num, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(hands_num)]


def best_hand(hand):
    return all_max([list(x) for x in combinations(hand, 5)], key=hand_rank)


def all_max(iterable, key=None):
    result, max_rank = [], None
    key = key or (lambda x:x)
    for x in iterable:
        x_rank = key(x)
        if not result or x_rank > max_rank:
            result, max_rank = [x], x_rank
        elif x_rank == max_rank:
            result.append(x)
    return result


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => hand"""
    return all_max(hands, key=hand_rank)


def group(items):
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


count_ranking = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3,
                 (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def hand_rank(hand):
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = zip(*groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    flush = len(set([s for r, s in hand])) == 1
    straight = max(ranks) - min(ranks) == 4 and len(set(ranks)) == 5
    return max(count_ranking[counts], 5*flush + 4*straight), ranks


def hand_percentage(n=700000, names=hand_names):
    counts = [0] * 9
    for i in range(int(n/10)):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for j in reversed(range(9)):
        print("%14s: %6.3f %%" % (names[8-j], 100.*counts[j]/n))


def p2p(games_num=5):
    result = []
    for i in range(games_num):
        deals = deal(2)
        if len(poker(deals)) > 1: break
        winner = deals.index(poker(deals)[0])
        result.append(winner)
        print(deals)
        if winner == 0: print('Player1 win.')
        else: print('Player2 win.')
    p1, p2 = result.count(0), result.count(1)
    if p1 > p2:
        print('Winner is %s, won %d out of %d games!' % ('Player1', p1, games_num))
    elif p1 < p2:
        print('Winner is %s, won %d out of %d games!' % ('Player2', p2, games_num))
    else:
        print('Two players tied!')


def normal_mode(player_num=6):
    while input('Press "enter" to start poker. Press "q" to quit:') != 'q':
        deals = deal(player_num)
        winner = poker(deals)
        print(deals)
        print(winner, hand_rank(winner[0]))
        print('\n')



#p2p(8)
#normal_mode(4)
hands = deal(5, 7)
print(hands)
best_hands = [best_hand(hand)[0] for hand in hands]
print(poker(best_hands))