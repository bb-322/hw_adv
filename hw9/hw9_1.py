def sped(length_m: int | float, time_s: int | float) -> int:
    return length_m / time_s

length_m = 1
time_s = 1

def test_sped():
    assert isinstance(length_m, (int, float)), 'invalid annotation'
    assert isinstance(time_s, (int, float)), 'invalid annotation'
    assert length_m >= 0, 'invalid length'
    assert time_s >= 0, 'invalid time'
    assert sped(length_m, time_s) >= 0, 'invalid data'