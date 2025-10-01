import pytest
from pytest import approx
from water_flow import water_column_height

def test_water_column_height():
    assert water_column_height(0, 0) == approx(0, abs = 0.001)
    assert water_column_height(0, 10) == approx(7.5, abs = 0.001)
    assert water_column_height(25, 0) == approx(25, abs = 0.001)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs = 0.001)

pytest.main(["-v", "--tb=line", "-rN", __file__])