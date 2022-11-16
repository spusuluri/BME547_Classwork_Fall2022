import pytest
from database_definition import Patient


def test_add_patient():
    from db_server import add_patient, init_server
    init_server()
    patient_name = "David"
    patient_id = 222
    blood_type = "A+"
    answer = add_patient(patient_name, patient_id, blood_type)
    find_patient = Patient.objects.raw({"_id": 222}).first()
    find_patient.delete()
    assert answer.name == patient_name


def test_add_test_info():
    from db_server import init_server, add_patient, add_test_info
    patient_id = 123
    patient_name = "David"
    added_patient = add_patient(patient_name, patient_id, "A+")
    test_name = "XXX"
    test_result = 200
    out_data = {
        "id": patient_id,
        "test_name": test_name,
        "test_result": test_result
    }
    answer = add_test_info(out_data)
    patient_from_db = Patient.objects.raw({"_id": patient_id}).first()
    added_patient.delete()
    assert patient_from_db.test_name[-1] == test_name
    assert patient_from_db.test_result[-1] == test_result
