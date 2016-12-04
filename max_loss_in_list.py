# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 15:27:51 2016

@author: Maciej Sołtysiak

Coding game solution of probelm:

A finance company is carrying out a study on the worst stock 
investments and would like to acquire a program to do so. 
The program must be able to analyze a chronological series of stock 
values in order to show the largest loss that it is possible to 
make by buying a share at a given time t0 and by selling it at a later date t1.
The loss will be expressed as the difference in value between t0 and t1.
If there is no loss, the loss will be worth 0.
"""

import sys
import math



def max_loss_calc(values):
    max_loss = 0
    profit = 0
    open_val = 0
    close_val = sys.maxint
    for i in values:    
        v = int(i)
        # If current price is higher than past open price max , 
        # If new highest open position found, set close position and open position to current value
        if v > open_val:
            open_val = v
            close_val = v
        if v < close_val:
            close_val = v
        profit= close_val - open_val
        max_loss = min(profit , max_loss)
    return max_loss


if __name__ == '__main__':
    values  = [1,2, 0]
    print max_loss_calc(values)
