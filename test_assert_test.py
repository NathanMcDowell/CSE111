

import pytest
from pytest import approx
from assert_test import calculate_rectangle_area


def test_calculate_rectangle_area():
    assert calculate_rectangle_area(10, 10) == 100

pytest.main(["-v", "--tb=line", "-rN", __file__])