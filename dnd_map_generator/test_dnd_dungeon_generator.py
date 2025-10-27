import pytest
from dnd_dungeon_generator import gen_starting_area, gen_stairs, gen_doors, gen_beyond_door

def test_gen_starting_area():
    assert gen_starting_area("1") == "Square, 20 x 20ft.; passage on each wall"
    assert gen_starting_area("10") == "Passage, 10ft. wide; four-way intersection"

def test_gen_stairs():
    assert gen_stairs("1-4") == "Down one level to a chamber"
    assert gen_stairs("20") == "Shaft (with or without elevator) up one level to a chamber and down one level to a chamber"

def test_gen_doors():
    assert gen_doors("1-10") == "Wooden"
    assert gen_doors("20") == "Secret door; barred or locked"

def test_gen_beyond_door():
    assert gen_beyond_door("1-2") == "Passage extending 10ft., then T intersection extending 10ft. to the right and left"
    assert gen_beyond_door("20") == "False door with trap"


pytest.main(["-v", "--tb=line", "-rN", __file__])