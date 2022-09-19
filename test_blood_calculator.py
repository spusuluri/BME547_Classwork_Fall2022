import pytest
@pytest.mark.parametrize("HDL_value, expected",
[(85, "Normal"), (50, "Borderline Low"), (30, "Low")])

def test_check_HDL(HDL_value, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_value)
    assert answer == expected

@pytest.mark.parametrize("LDL_value, expected",[(200, "Very High"), (185, "High") , (130, "Borderline High"), (100, "Normal")])

def test_check_LDL(LDL_value, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_value)
    assert answer == expected

@pytest.mark.parametrize("total_cholesterol_value, expected",[(240, "High"), (225, "Borderline High") , (100, "Normal")])

def test_check_total_cholesterol(total_cholesterol_value, expected):
    from blood_calculator import check_total_cholesterol
    answer = check_total_cholesterol(total_cholesterol_value)
    assert answer == expected