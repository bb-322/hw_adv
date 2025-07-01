import pytest

def bmi(mass:int | float, height:int | float):
    

    assert isinstance(mass, (int, float)), 'invalid annotation'
    assert isinstance(height, (int, float)), 'invalid annotation'
    assert 0 < mass < 1000, 'invalid mass'
    assert 0 < height < 1000, 'invalid height'

    bmi = mass / ((height/100)**2)
    
    if 18 < bmi <= 25:
        return 'avg mass'
    
    elif bmi <= 18:
        return 'need more mass'
    
    elif bmi > 25:
        return 'fat'

@pytest.mark.parametrize("mass, height, err_msg", [
    ('123', 10, 'invalid annotation'),
    (10, '123', 'invalid annotation'),
    (0, 100, 'invalid mass'),
    (100, 0, 'invalid height'),
    (1000, 10, 'invalid mass'),
    (10, 1000, 'invalid height')
])
def test_bmi_values(mass, height, err_msg):
    with pytest.raises(AssertionError, match=err_msg):
        bmi(mass, height)