import pytest
@pytest.mark.parametrize("HDL_value, expected",
[(85, "Normal"), (50, "Borderline Low"), (30, "Low")])

def test_check_HDL(HDL_value, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_value)
    assert answer == expected
