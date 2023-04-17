#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 07:19:12 2023

@author: carsonellsworth
"""
import curses
import time
import random as rng
from automata_rules import Rules
import automata_rules
POPULATED_CELL_CHAR = "*"
EMPTY_CELL_CHAR = " "
SLEEP_TIME = .5

def automata_visualizer(stdscr,machine:Rules):
    for i in range(machine.bounds[0]):
        for j in range(machine.bounds[1]):
            if(machine.matrix[i][j] == 1):
                stdscr.addch(i,j, POPULATED_CELL_CHAR)
            else:
                stdscr.addch(i,j, EMPTY_CELL_CHAR)
                pass
    
    

# Clear Screen
def main(stdscr):
    curses.start_color()
    stdscr.clear()
    dim = curses.LINES, curses.COLS#screen dimensions in x,y
    #-1 is quick fix for curses bottom right being unwritable
    matrix = [[rng.randint(0,1) for _ in range(dim[1]-1)] for _ in range(dim[0]-1)]
    
    
    mach = automata_rules.Automata3(matrix)
    try:
        while True:
            automata_visualizer(stdscr,mach)
            stdscr.refresh()
            mach.time_step()
            time.sleep(SLEEP_TIME)
    except(KeyboardInterrupt):
        pass
    
    
curses.wrapper(main)