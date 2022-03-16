#-----IMPORTING-----
from Evolution import *
import pytest

#-----TESTING-----

def test_evolution_commutation():
    assert evolve(evolve('0')) == evolve('000')

def test_bynary_convertion():
    assert from_bynary_to_state(bin(30)) == '   0000 '

def test_rule_generation():
    rule_keys = ['   ', '00 ', '0 0', '0  ', ' 00', ' 0 ', '  0', '000']
    rule = generate_rule(30)

    for i in range(8):
        assert rule[rule_keys[i]] == from_bynary_to_state(bin(30))[i]
