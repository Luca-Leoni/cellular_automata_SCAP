#-----IMPORTING-----
import numpy as np
import string
import pytest

#-----CONSTANTS-----

rule30 = {
        '   ': ' ',
        '00 ': ' ',
        '0 0': ' ',
        '0  ': '0',
        ' 00': '0',
        ' 0 ': '0',
        '  0': '0',
        '000': ' '
        }

#-----FUNCTIONS-----

####################
# generate the first
# state, simply
def generate_state():
    return '0'

####################
# generate the next
# step in the sequency
# following the 30 rules
def evolve(state):
    new_state = '0'
    state_lenght = len(state)

    for i in range(0, state_lenght):
        # Extracting the subsequence
        subsequence = ''
        
        if i != 0:
            subsequence += state[i-1]
        else:
            subsequence += ' '

        subsequence += state[i]

        if i != state_lenght - 1:
            subsequence += state[i+1]
        else:
            subsequence += ' '

        # Add the corresponding value in the rule30
        new_state += rule30[subsequence]

    new_state += '0'

    return new_state


###########MAIN###########
# core of the simulation
# generate that state and 
# evolve it for n_steps times
def simulation(n_steps):
    states = [generate_state()]
    
    for i in range(n_steps):
        states.append(evolve(states[-1]))

    return states

#########################
# function to print out
# the simulation output
# in a nice style
def printa(n_steps):
    states = simulation(n_steps)

    for i in range(n_steps):
        righe = ''
        for j in range(i, n_steps):
            righe += ' '

        print(righe + states[i] + righe)

printa(20)


#-----TESTING-----

def test_evolution_function():
    assert evolve('0') == '000'
    assert evolve('000') == '00  0'
    assert evolve(evolve('0')) == evolve('000')
