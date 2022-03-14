#-----TESTING-----

def test_evolution_function():
    assert evolve('0') == '000'
    assert evolve('000') == '00  0'
    assert evolve(evolve('0')) == evolve('000')
