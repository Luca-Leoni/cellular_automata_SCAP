#-----IMPORTING-----
import numpy as np
import string

#-----FUNCTIONS-----

#########################
# functio to transform 
# a bynary to a state
def from_bynary_to_state(bynary):
    state = bynary.replace("b", "").replace("0", " ").replace("1", "0")

    # Need to have 8 entries
    while len(state) < 8:
        state = " " + state

    return state 

#########################
# function to generate
# the rule associated
# to a particular integer
def generate_rule(num: int):
    rule_keys = ['   ', '00 ', '0 0', '0  ', ' 00', ' 0 ', '  0', '000']
    
    # Transform the number in binary and transform in an array of 0 and spaces
    state_rapr = list(from_bynary_to_state(bin(num)))
 
    # generate the dictionary using implicit for
    #return {rule_keys[i]: bynary_rapr[i] for i in range(len(bynary_rapr))}
    return dict(zip(rule_keys, state_rapr))

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
        new_state += generate_rule(110)[subsequence]

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



#printa(20)

#print(generate_rule(110))
