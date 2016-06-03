# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 10:54:36 2016

@author: IEn Gdańsk
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
p1_deck = []
p2_deck = []
result = []
number_of_rounds = 0
suit_order = {'D':0,'H':1,'C':2,'S':3}
card_order = {}
for i in range(2,10):
    card_order[i] = i
dic1 = {'J':11,'Q':12,'K':13,'A':14}
card_order.update(dic1)


def compare_suit(card1_suit,card2_suit):
    if suit_order[card1_suit] > suit_order[card2_suit]:
        return 1
    elif suit_order[card1_suit] < suit_order[card2_suit]:
        return 2
    else:
        return 3

def compare_cards(p1_card,p2_card):
    winner_id = 0
    if (p1_card[0] != p2_card[0]):
        if card_order[p1_card[0]] > card_order[p2_card[0]]:
            winner_id = 1
        else:
            winner_id = 2        
    else:
        winner_id=compare_suit(p2_card[1],p2_card[1]) 
    print('Winner id: %d' %winner_id)
    return winner_id

def war_card(p1_deck,p2_deck):
    number_of_rounds = 0
    while (p1_deck and p2_deck):
        number_of_rounds += 1
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)
        if(compare_cards(p1_card,p2_card) == 1):
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        if(compare_cards(p1_card,p2_card) == 2):
            p2_deck.append(p1_card)
            p2_deck.append(p2_card)
        print(p1_deck)
        print(p2_deck)
        print('-----')
    if p1_deck:
        winner = 1
    else:
        winner = 2
    return ''.join([str(winner),' ',str(number_of_rounds)])
#test case 1
p1_deck = ['AD', 'KC', 'QC']
p2_deck = ['KH', 'QS', 'JC']
#==============================================================================
# n = int(input())  # the number of cards for player 1
# for i in range(n):
#     cardp_1 = input()  # the n cards of player 1
#     p1_deck.append(cardp_1)
# m = int(input())  # the number of cards for player 2
# for i in range(m):
#     cardp_2 = input()  # the m cards of player 2
#     p2_deck.append(cardp_2)
#==============================================================================

str_print = "player1_deck" + str(p1_deck) + "\n" + "player2_deck" + str(p2_deck)
print(str_print)
print(card_order)
#print(str_print, file=sys.stderr)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
result = war_card(p1_deck,p2_deck)
final_result = result
print(final_result)
